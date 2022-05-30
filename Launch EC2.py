import boto3
client = boto3.client('ec2')
response = client.run_instances(ImageId='ami-0022f774911c1d690' ,
                                InstanceType='t2.micro' ,
                                MinCount=1 ,
                                MaxCount=1)
for Instance in response ['Instances']:
    print(Instance['InstanceId'])