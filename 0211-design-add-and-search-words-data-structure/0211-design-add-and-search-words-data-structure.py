class TreeNode():
    def __init__(self):
        self.childern={}
        self.end=False

class WordDictionary(object):

    def __init__(self):
        self.root=TreeNode()
        

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        cur=self.root
        for c in word:
            if c not in cur.childern:
                cur.childern[c]=TreeNode()
            cur=cur.childern[c]
        cur.end=True

        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        def dfs(j,root):
            cur=root
            for i in range(j,len(word)):
                c=word[i]
                if c==".":
                    for child in cur.childern.values():
                        if dfs(i+1,child):
                            return True
                    return False
                else:
                    if c not in cur.childern:
                        return False
                    cur=cur.childern[c]
            return cur.end
        return dfs(0,self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)