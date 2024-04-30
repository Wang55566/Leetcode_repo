class Solution:
  def __init__(self):
    self.ingestion_data = {}
    self.length = 0

  def ingest(self, tokens):
    self.length += 1
    token_parse = tokens.split(":")

    curr = self.ingestion_data

    for i in range(len(token_parse)):
      if token_parse[i] not in curr:
        curr[token_parse[i]] = {'count': 1}
      else:
        curr[token_parse[i]]['count'] = 1

      curr = curr[token_parse[i]]

  def appearance(self, input):
    pass

solution = Solution()

solution.ingest("token1:token2:token3")
solution.ingest("token1:token10")
solution.ingest("token1:token10")
solution.ingest("token1:token1")
solution.appearance("token1:token10")

solution.ingest('oursky:uk:dev')
solution.ingest('oursky:hk:design')
solution.ingest('oursky:hk:pm')
solution.ingest('oursky:hk:dev')
solution.ingest('skymaker')
solution.appearance('oursky')
# > 0.8
solution.appearance('oursky:hk')
# > 0.6
solution.ingest('skymaker:london:ealing:dev')
solution.ingest('skymaker:london:design')
solution.ingest('skymaker:london:design')
solution.ingest('skymaker:man:pm')
solution.ingest('skymaker:man:pm')
solution.appearance('skymaker:man')
# > 0.2
solution.appearance('skymaker:lon')
# > 0
solution.appearance('london:skymaker')
# > 0
