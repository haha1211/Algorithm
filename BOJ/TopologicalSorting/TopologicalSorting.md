# Topological Sorting

## Topological Sorting이란?
+ 위상 정렬
+ 순서가 정해져 있는 작업을 차례대로 수행해야 할 때 사용하는 알고리즘

## Topological Sorting의 특징
+ DAG(Directed Acyclic Graph)에서만 적용 가능
    - cycleX, 방향O graph
    - cycle 있는 경우 => 시작점 찾을 수 X
+ 여러 가지 답 존재 가능
    - 처음 queue에 indegree가 0인 node를 찾아 추가할 때, 해당 node가 여러 개인 경우

## Topological Sorting의 동작 과정(BFS 활용)
1. indegree(진입차수)가 0인 node를 queue에 추가
2. queue가 빌 때까지 아래 과정 반복
    1. queue에서 node를 꺼낸 후, 해당 node에서 나가는 edge를 graph에서 제거
    2. 새롭게 indegree가 0인 node를 queue에 추가

## Topological Sorting의 시간 복잡도
+ 인접리스트 사용하는 경우 : O(V+E)


