from server_backup.bags import BagWriter


class BagFixer(BagWriter):
    header_not_set = []
    name = '[BagFixer]'

    def task(self, val):
        if val:
            topic = val[0]
            msg = val[1]
            time = val[2]
            if msg._has_header:
                if msg.header.stamp.secs > 0:
                    self.add(topic, msg, msg.header.stamp)
                else:
                    if topic not in self.header_not_set:
                        self.logger(error=f"{self.name}: Header is not set correctly {topic}! Use datalogger time. Take care next time.")
                        self.header_not_set.append(topic)
                    msg.header.stamp = time
                    self.add(topic, msg, time)
            else:
                if '/velodyne_packets' == topic:
                    self.add(topic, msg, msg.stamp)
                elif '/tf' == topic and msg.transforms:
                    self.add(topic, msg, msg.transforms[0].header.stamp)
                else:
                    self.add(topic, msg, time)

    def cleanup(self):
        self.bag.close()
        self.logger(debug=f"{self.name}: Finish writing fixed {self.path} bagfile.")
