import boto3
client = boto3.client('ec2')
response = client.terminate_instances(InstanceIds=['i-097dd82aabe409acd'])

for instances in response['TerminatingInstances']:
    print("Deleted Instance ID is {}".format(instances['InstanceId']))