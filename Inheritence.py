# i
class MobilePhone:
    def __init__(self, screen_type, network_type, dual_sim,
                 front_camera, rear_camera, ram, storage):
        self.screen_type = screen_type
        self.network_type = network_type
        self.dual_sim = dual_sim
        self.front_camera = front_camera
        self.rear_camera = rear_camera
        self.ram = ram
        self.storage = storage

    def make_call(self, number):
        print(f"Calling {number}...")

    def receive_call(self):
        print("Receiving a call...")

    def take_picture(self):
        print(f"Taking picture with {self.rear_camera} rear camera")


# ii
class Apple(MobilePhone):
    def __init__(self, front_camera, rear_camera, ram, storage):
        super().__init__(
            "Touch Screen",
            "5G",
            False,
            front_camera,
            rear_camera,
            ram,
            storage
        )

    def apple_feature(self):
        print("Using Apple exclusive feature (Face ID)")


# iii
class Samsung(MobilePhone):
    def __init__(self, front_camera, rear_camera, ram, storage):
        super().__init__(
            "Touch Screen",
            "4G/5G",
            True,
            front_camera,
            rear_camera,
            ram,
            storage
        )

    def samsung_feature(self):
        print("Using Samsung exclusive feature (Secure Folder)")


# iv
iphone1 = Apple("12MP", "48MP", "4GB", "64GB")
iphone2 = Apple("16MP", "32MP", "3GB", "128GB")

samsung1 = Samsung("8MP", "48MP", "4GB", "64GB")
samsung2 = Samsung("12MP", "32MP", "3GB", "128GB")


# v
iphone1.make_call("9876543210")
iphone1.take_picture()
iphone1.apple_feature()

print()

samsung1.receive_call()
samsung1.take_picture()
samsung1.samsung_feature()
