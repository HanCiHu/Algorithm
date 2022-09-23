from collections import defaultdict
import math

def solution(fees, records):
    answer = []
    cars = {}
    totalParkingTime = defaultdict(lambda: 0)
    visit = {}
    fee = {}
    for record in records:
      info = record.split(' ')
      time = info[0].split(':')
      totalTime = int(time[0]) * 60 + int(time[1])
      car_id = int(info[1])

      if info[2] == 'IN':
        cars[car_id] = (totalTime)
        visit[car_id] = True
        totalParkingTime[car_id] += 0
      elif info[2] == 'OUT':
        totalParkingTime[car_id] += (totalTime - cars[car_id])
        visit[car_id] = False
  
    sortedParkingTime = sorted(totalParkingTime.items())
    for i in sortedParkingTime:
      parkingTime = (23 * 60 + 59) - cars[i[0]] + i[1] if visit[i[0]] else i[1]
      answer.append(fees[1] if parkingTime <= fees[0] else fees[1] + (math.ceil((parkingTime - fees[0]) / fees[2])) * fees[3])
    return answer


print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))

#  if (parkingTime <= fees[0]):
#           fee[car_id] += fees[1]
#         else:
#           fee[car_id] += fees[1] + ((parkingTime - fees[0]) // fees[2]) * fees[3]