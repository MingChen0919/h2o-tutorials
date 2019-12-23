import h2o

h2o.init(nthreads=-1)

df = h2o.import_file(path='../data/titanic.csv')
df.types

# convert some integer columns to factor/categorical
df['survived'] = df['survived'].asfactor()
df['ticket'] = df['ticket'].asfactor()



# set predictors and response variable
response = 'survived'
predictors = df.columns
predictors.remove('survived')
predictors.remove('name')
predictors.remove('ticket')
predictors.remove('home.dest')
print(response)
print(predictors)

splits = df.split_frame(ratios=[0.6, 0.2],
                        destination_frames=['train.hex', 'valid.hex', 'test.hex'],
                        seed=1234)

train = splits[0]
valid = splits[1]
test = splits[2]
h2o.cluster().shutdown()
