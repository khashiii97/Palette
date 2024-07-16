from collections import defaultdict
from matplotlib import pyplot as plt

import  numpy as np
#super-matrix 
maxs = np.load("maxs.npy",allow_pickle=True)
label_set = np.load("label_to_setnum_1000_5_1.npy",allow_pickle=True) # it is a dict like {20: [0], 29: [0], ...} where each website is assigned to a list of clusters

label_set = label_set.tolist()

plt.rcParams["font.family"] = "Times New Roman"
cluster_num = 19
def euclidean(x, y):
    dist = np.sqrt(np.sum(np.square(x - y)))
    return dist
def DistanceList(maxs,label_set): # it seems it returns a list of lists, each list containing the supermatrices in a cluster
    print(type(label_set))
    distance = []
    for i in range(cluster_num):
        distance_list = []
        for key,value in label_set.items():
            if value[0] == i:
                distance_list.append(maxs[key])
        distance.append(distance_list)
    return distance
def CalInDistance(distance):
    dis_mean_res = []
    for i in range(cluster_num):
        distance_cluster = distance[i]
        distance_res = []
        for j in range(len(distance_cluster)):
            for k in range(j + 1, len(distance_cluster)):
                # sim = dtw(x=f1, y=f2, dist_method='euclidean', keep_internals=True)
                sim = euclidean(distance_cluster[j], distance_cluster[k])
                distance_res.append(sim)
        dis_mean_res.append(np.mean(distance_res))
    return dis_mean_res
distance = DistanceList(maxs,label_set)

def CalInterDistance(distance):
    dis_res = []

    for i in range(cluster_num):
        dis_res_each = []

        for j in range(cluster_num):
            if i == j:
                continue
            distance_1 = distance[i]
            distance_2 = distance[j]
            for k in range(len(distance_1)):
                for l in range(len(distance_2)):
                    sim = euclidean(distance_1[k], distance_2[l])
                    dis_res_each.append(sim)
        dis_res.append(dis_res_each)
        print(len(dis_res_each))
    return dis_res

if __name__ == '__main__':

    distance_mean = CalInDistance(distance)
    distance_res_inter = CalInterDistance(distance)
    print(distance_mean)
    #print(distance_res_inter)
    plt.figure(figsize=(12,4))
    plt.xticks(fontsize = 20)

    plt.yticks(fontsize = 20)
    plt.subplots_adjust(left=0.15, right=0.95, top=0.9, bottom=0.2)


    plt.boxplot(distance_res_inter,
                showfliers=False,
                labels=[str(i) for i in range(1, cluster_num + 1)],
                medianprops={"color": "red", "linewidth": 1},  # 设置中位数的属性，如线的类型、粗细等
                boxprops={"color": "red", "linewidth": 1},  # 设置箱体的属性，如边框色，填充色等
                whiskerprops={"color": "red", "linewidth": 1},  # 设置须的属性，如颜色、粗细、线的类型等
                capprops={"color": "red", "linewidth": 1})
    #plt.title('Boxplot Example')
    plt.ylabel('Distance',fontsize = 20)
    plt.xlabel('Anonymity Set Index',fontsize = 20)
    for i in range(len(distance_mean)):
        plt.plot(i+1, distance_mean[i], marker = "*",color = "blue",markersize = 9)
    custom_legend = [
    plt.Line2D([0], [0], marker='*', color='w', markerfacecolor='blue', markersize=15, label='Intra-cluster Distance'),
]
    plt.grid(axis="y", linestyle='--')
    plt.legend(handles=custom_legend,fontsize = 20,loc = "upper right")
    plt.gca().spines['top'].set_linewidth(2)  # 设置顶部边框粗细为2
    plt.gca().spines['right'].set_linewidth(2)  # 设置右侧边框粗细为2
    plt.gca().spines['bottom'].set_linewidth(2)  # 设置底部边框粗细为2
    plt.gca().spines['left'].set_linewidth(2)  # 设置左侧边框粗细为2
   



    plt.show()

