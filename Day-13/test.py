import boto3

client = boto3.client('s3')

# Create a bucket in S3 using boto3 python library
# response = client.create_bucket( 
#     Bucket='mydemo-boto3'
# )

response = client.get_object_acl(
    Bucket='mydemo-boto3',
)

print(response)