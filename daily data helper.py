class DailyDataHelper:
    def __init__(self):
        self.data = ["Milk", "Bread", "Eggs", "Rice"]
        print("Daily Data Helper Started")

    def show_data(self):
        print("\nDaily Data:")
        for i, item in enumerate(self.data):
            print(i, "-", item)

    def search(self, value):
        for i, item in enumerate(self.data):
            if item == value:
                print(value, "found at index", i)
                return
        print(value, "not found")

    def __del__(self):
        print("Daily Data Helper Ended")


obj = DailyDataHelper()
obj.show_data()
obj.search("Eggs")
obj.search("Apple")

del obj