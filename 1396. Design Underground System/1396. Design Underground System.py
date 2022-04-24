class UndergroundSystem(object):

    def __init__(self):
        # record the customer's starting trip
        # card ID: [station, t]
        self.customer_trip = {}

        # record the average travel time from start station to end station
        # (start, end): [t, times]
        self.trips = {}

    def checkIn(self, id, stationName, t):
        self.customer_trip[id] = [stationName, t]

    def checkOut(self, id, stationName, t):
        # get the check in information of the customer
        start_station, start_t = self.customer_trip[id]
        del self.customer_trip[id]

        # the trip information
        # stationName => end_station
        # t => end_t
        trip = (start_station, stationName)
        travel_time = t - start_t

        # store / update the trip information
        if trip not in self.trips:
            self.trips[trip] = [travel_time, 1]
        else:
            # another way to write that is store the total traveling time and the number of travels
            # so that you do not need to calculate the avg time everytime
            avg_t, times = self.trips[trip]
            self.trips[trip] = [
                (avg_t * times + travel_time) / (times + 1.0), times + 1]

    def getAverageTime(self, startStation, endStation):
        return self.trips[(startStation, endStation)][0]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
