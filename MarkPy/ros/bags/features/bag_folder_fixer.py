from server_backup.threads import GeneralWorker, Channel
from server_backup.terminator import Terminator
from server_backup.watcher import adjust_absolute_path
from server_backup.bags import BagReader
from .bag_fixer import BagFixer
from pathlib import Path
from os import remove

# Changes:
# Input folder -
# Output folder
# Adjust the path for each bags to the new target folder


class BagFolderFixer:
    def __init__(self, input_folder, dest_folder, logger, concurrent=3, delete_previous=False):
        self.name = '[BagFolderFixer]'
        self.logger = logger
        self.input_folder = input_folder
        self.dest_folder = dest_folder

        self.bags_to_process = []
        for bag in list(Path(self.input_folder).glob('**/*.bag')):
            self.bags_to_process.append({'input': bag.absolute(),
                                        'output': adjust_absolute_path(bag, self.input_folder, self.dest_folder)})

        self.logger(debug=f"{self.name}: founded {len(self.input_folder)} bags")
        self.delete_prev = delete_previous
        self.logger=logger
        self.max_concurrent = concurrent
        self.threads = []

    def start(self):
        while len(self.bags_to_process) > 0:
            for x in range(self.max_concurrent):
                if len(self.bags_to_process) > 0:
                    bag_to_process = self.bags_to_process.pop()
                    self.logger(debug=f"{self.name}: Creating fixer thread: {bag_to_process['input']}")
                    th = BagFixerProcess(bag_to_process['input'], bag_to_process['output'], self.logger, 0, 330 * x, self.delete_prev)
                    self.threads.append(th)

            for thread in self.threads:
                self.logger(debug=f"{self.name}: Starting fixer thread")
                thread.start()

            for y in range(self.max_concurrent):
                if len(self.threads) > 0:
                    thread = self.threads.pop()
                    thread.join()
                    self.logger(debug=f"{self.name}: Terminated fixer thread")

class BagFixerProcess(GeneralWorker, Terminator):
    def __init__(self, input_bag, output_bag, logger, x, y, delete_prev=False):
        GeneralWorker.__init__(self, logger)
        Terminator.__init__(self, logger, x, y, 800, 250)
        self.name = '[BagFixerProcessShell]'
        self.input_bag = input_bag
        self.output_bag = output_bag
        self.delete_prev = delete_prev
        self.process = None

    def init(self):
        self.logger(debug=f"{self.name}: Initialization")
        self.logger(debug=f"{self.name}: Source: {self.input_bag}")
        self.logger(debug=f"{self.name}: Destination: {self.output_bag}")


    def task(self):
        # Create Channel
        channel = Channel()
        # Create Bag reader
        reader = BagReader(self.input_bag, channel, self.logger)
        # Create Bag writer
        writer = BagFixer(self.output_bag, channel, self.logger)
        # Start workers
        reader.start()
        writer.start()
        # Wait workers
        reader.join()
        writer.join()
        self.logger(debug=f'[{__name__}]: Bag feature fixer Done')

        # self.run_process(f"server_bag fixer -i {self.input_bag} -o {self.output_bag}")
        # self.set_finish()
        # if self.delete_prev:
        #     self.logger(debug=f"{self.name}: Removing original bag: {self.input_bag}")
        #     remove(self.input_bag)

    def cleanup(self):
        self.logger(debug=f"{self.name}:  Fixer finished. Produced bag: {self.output_bag}")
