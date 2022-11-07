import topcv
import ITViec
import vietnamworks

print("Thành phố:", end=" ")
province = "ha noi"
print("Từ khóa:", end=" ")
jobInput = "reactjs"
# print("Lương(USD):", end=" ")
# salary = int(input())

# print("-----------ITViec------------")
ITViec.itviecTotal(province, jobInput)
# ITViec.getAllJob()
ITViec.recommendJob()

# print("-----------TopCV------------")
topcv.topcvTotal(province, jobInput)
# topcv.getAllJob()
topcv.recommendJob()

# print("-----------VietNamWorks------------")
vietnamworks.vietnamworksTotal(province, jobInput)
vietnamworks.recommendJob()
