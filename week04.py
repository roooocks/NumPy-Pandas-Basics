import pandas as pd

scores = [100, 97, 88, 91]
average = pd.Series(scores).min()
print(average) # git push -f origin main은 주의 필요 (원격 리포지토리를 로컬 리포지토리로 덮어씀)
