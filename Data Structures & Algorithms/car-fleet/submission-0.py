class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(position[i], speed[i]) for i in range(len(position))]
        cars.sort(key = lambda car: -car[0])
        # print(cars)
        s = []

        for car in cars:
            if s:
                pos_leading_car = s[-1][0]
                speed_leading_car = s[-1][1]
                pos_chasing_car = car[0]
                speed_chasing_car = car[1]
                time_to_target = (target - pos_leading_car) / speed_leading_car
                can_catch = pos_chasing_car + speed_chasing_car * time_to_target >= target
                # print(can_catch)
                if not can_catch:
                    s.append(car)
            else: s.append(car)

        return len(s)