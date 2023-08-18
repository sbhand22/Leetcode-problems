class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap={i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            preMap[crs].append(pre)
        visiting = set()
        def dfs(crs):
            if crs in visiting:
                return False
            if preMap[crs]==[]:
                return True
            visiting.add(crs)
            for p in preMap[crs]:
                if not dfs(p):
                    return False
            visiting.remove(crs)
            preMap[crs]=[]
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
