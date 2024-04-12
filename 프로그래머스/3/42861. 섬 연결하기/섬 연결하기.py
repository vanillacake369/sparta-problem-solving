# 가장 적은 간선비용으로 모든 노드 연결 -> 크루스칼 알고리즘,,,
def solution(n, costs):
    sortedByCost = sorted(costs, key=lambda x: x[2])
    nodes = set([sortedByCost[0][0]])
    minCostSum = 0
    while len(nodes) != n:
        for eachNode in sortedByCost:
            if eachNode[0] in nodes and eachNode[1] in nodes:
                continue
            if eachNode[0] in nodes or eachNode[1] in nodes:
                nodes.update([eachNode[0], eachNode[1]])
                minCostSum += eachNode[2]
                break
    return minCostSum