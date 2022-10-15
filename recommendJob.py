import topcv
import ITViec
import vietnamworks

print("Thành phố:", end=" ")
province = input()
print("Từ khóa:", end=" ")
jobInput = input()
print("Lương(USD):", end=" ")
salary = int(input())

print("-----------ITViec------------")
ITViec.itviecTotal(province, jobInput)
ITViec.recommendJob(salary)

print("-----------TopCV------------")
topcv.topcvTotal(province, jobInput)
topcv.recommendJob(salary)

print("-----------VietNamWorks------------")
vietnamworks.vietnamworksTotal(province, jobInput)
vietnamworks.recommendJob(salary)