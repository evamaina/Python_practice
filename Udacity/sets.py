cities= ["kenya","nairobi","kisumu","uganda","kisumu","nairobi"]

print(set(cities))
print(list(set(cities)))


s = set[1,2,3,4]
s.add(4) # {1,2,3,4}

set1 = [1,2,3,4,5,6]
set1.remove(3) # {1,2,4,5,6}
set1.remove(8) # key error
set1.discard(5) # {1,2,4,6}



s1 = [1,2,3]
s2 = s1.copy # {1,2,3}

s3 = [1,2,3]
s3.clear  # set()


mathematics = {"peter","jane","john","james","eva"}
physics = {"john","eva","joyce","judy","james"}

mathematis | physics # {peter,jane,john,eva,james,joyce,judy} generates set with all unique values

mathematics & physics # {john,james,eva} generates set with values in both sets