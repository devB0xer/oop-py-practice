class Resource:

    def __init__(self, name: str, resource_type: str):
        self.name = name
        self.resource_type = resource_type

    def __del__(self):
        print(f"Resource {self.name}, type: {self.resource_type} has been deleted")


        