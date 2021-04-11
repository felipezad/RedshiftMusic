import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries
from botocore.exceptions import ClientError
import pandas as pd
import boto3
import json


def drop_tables(cur, conn):
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()
        
def createRole(KEY, SECRET, DB_IAM_ROLE_NAME):
   
    iam = boto3.client('iam',aws_access_key_id=KEY,
                     aws_secret_access_key=SECRET,
                     region_name='us-west-2'
                  )
    #1.1 Create the role, 
    try:
        print("1.1 Creating a new IAM Role") 
        dwhRole = iam.create_role(
            Path='/',
            RoleName=DB_IAM_ROLE_NAME,
            Description = "Allows Redshift clusters to call AWS services on your behalf.",
            AssumeRolePolicyDocument=json.dumps(
                {'Statement': [{'Action': 'sts:AssumeRole',
                   'Effect': 'Allow',
                   'Principal': {'Service': 'redshift.amazonaws.com'}}],
                 'Version': '2012-10-17'})
        )    
    except Exception as e:
        print(e)


    print("1.2 Attaching Policy")

    iam.attach_role_policy(RoleName=DB_IAM_ROLE_NAME,
                           PolicyArn="arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess"
                          )['ResponseMetadata']['HTTPStatusCode']

    print("1.3 Get the IAM role ARN")
    roleArn = iam.get_role(RoleName=DB_IAM_ROLE_NAME)['Role']['Arn']

    print(roleArn)

    
def createCluster():
    try:
        response = redshift.create_cluster(        
        #HW
        ClusterType=DWH_CLUSTER_TYPE,
        NodeType=DWH_NODE_TYPE,
        NumberOfNodes=int(DWH_NUM_NODES),

        #Identifiers & Credentials
        DBName=DWH_DB,
        ClusterIdentifier=DWH_CLUSTER_IDENTIFIER,
        MasterUsername=DWH_DB_USER,
        MasterUserPassword=DWH_DB_PASSWORD,
        
        #Roles (for s3 access)
        IamRoles=[roleArn]  
    )
    except Exception as e:
        print(e)

def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')
    
#     DB_IAM_ROLE_NAME       = config.get("IAM_ROLE", "DB_IAM_ROLE_NAME")  
#     KEY                    = config.get('AWS','KEY')
#     SECRET                 = config.get('AWS','SECRET')
#     createRole(KEY,SECRET,DB_IAM_ROLE_NAME)
    
    
    url = "host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values())
    print(url)
    
    conn = psycopg2.connect(url)
    cur = conn.cursor()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()