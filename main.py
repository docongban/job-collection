import ITViec
import topcv
import careerbuilder

print("Thành phố:", end=" ")
province = input()
print("Từ khóa:", end=" ")
keyword = input()

ITViec.recommend4Job(keyword, province)
topcv.recommend4Job(keyword, province)
careerbuilder.recommend4Job(keyword, province)