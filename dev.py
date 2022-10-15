import matplotlib.pyplot as plt
import numpy as np

import ITViec
import topcv
import topdev
import vietnamworks
import careerbuilder

import graph

print("Thành phố:", end=" ")
province = input()
print("Từ khóa:", end=" ")
jobInput = input()

# Get result
itviecResult = ITViec.itviecTotal(province,jobInput)
topcvResult = topcv.topcvTotal(province,jobInput)
topdevResult = topdev.topdevTotal(province,jobInput)
vietnamworksResult = vietnamworks.vietnamworksTotal(province,jobInput)
careerbuilderResult = careerbuilder.careerbuilderTotal(province,jobInput)

# print total
totalITViec = [int(s) for s in itviecResult.split() if s.isdigit()][0]
totalTopcv = [int(s) for s in topcvResult.split() if s.isdigit()][0]
totalTopdev = [int(s) for s in topdevResult.split() if s.isdigit()][0]
totalVietnamworks = [int(s) for s in vietnamworksResult.split() if s.isdigit()][0]
totalCareerbuilderResult = [int(s) for s in careerbuilderResult.split() if s.isdigit()][0]
print("Total ITViec: ", totalITViec)
print("Total Topcv: ", totalTopcv)
print("Total Topdev: ", totalTopdev)
print("Total Vietnamworks: ", totalVietnamworks)
print("Total Careerbuilder: ", totalCareerbuilderResult)

# Recommend Job
print("Lương(USD):", end=" ")
salary = int(input())
print("-----------ITViec------------")
ITViec.recommendJob(salary)
print("-----------TopCV------------")
topcv.recommendJob(salary)
print("-----------VietNamWorks------------")
vietnamworks.recommendJob(salary)

# Graph
x = np.array(["IT Viec", "Top CV", "Top Dev", "Vietnamworks", "Careerbuilder"])
y = np.array([totalITViec, totalTopcv, totalTopdev, totalVietnamworks, totalCareerbuilderResult])
graph.graphJobs(x, y)