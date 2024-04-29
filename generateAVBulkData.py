import random
import time
import uuid
import psycopg2

# Replace these variables with your connection details
db_name = 'thubsrv'
db_user = 'thubsrv_levJt6G0'
db_pass = '(AW5z+aWpv(uhP!opnEstAUz%JyX.4qx'
db_host = 'aurora-thubsrv-ap-northeast-1.cluster-csnwnzutgsmf.ap-northeast-1.rds.amazonaws.com'
db_port = '5432'

# Establish a connection to the database
conn = psycopg2.connect(
    dbname=db_name,
    user=db_user,
    password=db_pass,
    host=db_host,
    port=db_port
)

schema_name = 'thubsrv_threathub_aurora_unifiedfeed'
table_name = 'indicator_data'

def generate_random_data():
    data = []
    # Create a cursor object
    cur = conn.cursor()

    insert_query = f"""
        INSERT INTO thubsrv_threathub_aurora_unifiedfeed.indicator_data (threat_id, indicator_id, indicator_value, indicator_type, origin, operations, risk_level, confidence, galaxy_bulletin, galaxy_related_search, first_observed, last_observed, creation_time, last_modified_time, source_id, filter_name) values {data[_]};
        """

    count_query = f"""
        SELECT count (*) from thubsrv_threathub_aurora_unifiedfeed.indicator_data;
        """
    
    print("Total records in db before insert: " , cur.execute(count_query), cur.fetchone()[0])

    for _ in range(100000):
        threat_id = str(uuid.uuid4())
        indicator_id = str(random.randint(1000000000, 2000000000))  # Assuming indicator_id ranges from 3824880373 to 3824880393
        indicator_value = '.'.join(str(random.randint(0, 255)) for _ in range(4))  # Generate random IPv4 address
        #indicator_value = '161.178.223.179'
        indicator_type = 'ipv4'
        origin = random.choice(['China', 'USA', 'Germany', 'Australia', 'Japan', 'Brazil'])  # Sample countries
        operations = random.choice(['Jupter', 'Saturn', 'Mars', 'Neptune', 'Pluto'])  # Sample operations
        risk_level = 5  # Random risk level from 1 to 10
        confidence = 7  # Random confidence level from 1 to 10
        galaxy_bulletin = ''  # Placeholder for galaxy_bulletin
        galaxy_related_search = ''  # Placeholder for galaxy_related_search
        first_observed = int(time.time()) - random.randint(10000, 100000)  # Random value between 10,000 to 100,000 seconds ago
        last_observed = int(time.time())  # Current timestamp
        creation_time = int(time.time()) - random.randint(100000, 1000000)  # Random value between 100,000 to 1,000,000 seconds ago
        last_modified_time = int(time.time()) - random.randint(1000000, 2000000)  # Random value between 1,000,000 to 2,000,000 seconds ago
        source_id = 2
        filter_name = 'pakistan' 
        data.append((threat_id, indicator_id, indicator_value, indicator_type, origin, operations, risk_level, confidence, galaxy_bulletin, galaxy_related_search, first_observed, last_observed, creation_time, last_modified_time, source_id, filter_name))

 

        # Execute the query
        print("Inserting record no: ", {_} )
        cur.execute(insert_query)
    print(cur.execute(count_query))
    conn.commit()
    print("Total records in db after insert: " , cur.fetchone()[0])

    """
    # Print generated data (for verification)
    for record in generate_random_data():
        #print(record, ',')
        with open("av-bulk-data.log", 'a') as f:
            f.write(str(record)+",")
    """

if __name__ == "__main__":
    generate_random_data()
