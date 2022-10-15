import matplotlib.pyplot as plt
import numpy as np

def graphJobs(x,y):
    for i in range(len(x)):
        plt.text(i,y[i],y[i],ha = 'center')
    # plt.tight_layout()
    # plt.title('Thành phố: ' + province + ", Từ khóa:" + jobInput)
    plt.xlabel('Trang tuyển dụng')
    plt.ylabel('Tổng số lượng việc')
    plt.bar(x,y, color = ['#0b84a5', '#f6c85f', '#9dd866', '#6f4e7c', '#8dddd0'], width=0.35, alpha=0.7)
    plt.show()