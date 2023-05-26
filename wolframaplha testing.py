import wolframalpha

client = wolframalpha.Client('XEQ3GP-G74249KTGW')

while True:
    query = str(input('Query :'))
    res = client.query(query)
    output = next(res.results).text
    print(output)