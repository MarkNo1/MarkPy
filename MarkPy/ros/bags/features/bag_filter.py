from server_backup.bags import BagWriter


REPLAY_TOPICS = ['/avls_loc_output', '/awms_world_model', '/apfs_obstacles',
                 '/tf', '/tf_static', '/obstacles', '/nsdm_trajectory_ros', '/nsdm_info',
                 '/vehicleOdom', '/points_ground', '/points_nonground',
                 '/nav_space', '/vehicleSpeed', '/vehiclePath', '/obstacles_tracked']

SIMULATION_TOPICS = ['/velodyne_packets',  # Velodyne
                     '/mob_master/obstacles', '/mob_master/lane_markings', '/mob_master/traffic_lights',  # Mobileye
                     '/mob_master/traffic_signs',  # Mobileye
                     '/marben_lights',  # V2X
                     '/avls_loc_output', '/septentrio_fix',  # GPS
                     '/can_v_100hz', '/can_v_10hz', '/can_v_50hz']  # CAN


def get_topics(args):
    if args.topics:
        return args.topics.split(';')
    else:
        if args.mode == 'replay':
            self.logger(debug=f"Topics mode: REPLAY")
            return REPLAY_TOPICS
        if args.mode == 'simulation':
            self.logger(debug=f"Topic mode: SIMULATION")
            return SIMULATION_TOPICS
        else:
            self.logger(debug=f"Topics mode: UNDEFINED")
            return []


class BagFilterWriter(BagWriter):
    def __init__(self, bag_path,  topics_filter, channel, logger):
        BagWriter.__init__(self, bag_path, channel, logger)
        self.name = '[BagFilterWriter]'
        self.topics_filter = topics_filter

    def task(self, val):
        if val[0] in self.topics_filter:
            self.add(*val)

    def cleanup(self):
        self.bag.close()
        self.logger(debug=f"{self.name}: Finish writing filtered {self.path} bagfile")
