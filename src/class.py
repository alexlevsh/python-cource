class MyObject:
    class_attribute = 8
    class_test_attribute = 'text'

    def __init__(self):
        self.text = 'text32'
        self.data_attribute = 42

    def instance_method(self):
        print(self.data_attribute)
        print(self.text)

    @staticmethod
    def static_method():
        print(MyObject.class_attribute)

    @staticmethod
    def get_test():
        print(MyObject.class_test_attribute)


if __name__ == "__main__":
    MyObject.static_method()
    obj = MyObject()
    obj.instance_method()
    obj.static_method()
    obj.get_test()