def order(sentence):
  nums = [int(s) for s in sentence if s.isdigit()]
  # print(nums)
  words = sentence.split()
  # print(words)
  ordered = ' '.join([x for _,x in sorted(zip(nums,words))])
  # print(ordered)
  return ordered

order("4of Fo1r pe6ople g3ood th5e the2")
order("")
