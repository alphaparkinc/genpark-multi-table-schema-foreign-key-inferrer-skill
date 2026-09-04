from client import MultiTableSchemaForeignKeyInferrerClient

def main():
    client = MultiTableSchemaForeignKeyInferrerClient()
    res = client.infer_relational_schema()
    print('Foreign Key Inferrer: ' + res['inference_job_id'] + ' (Tables: ' + str(res['tables_analyzed']) + ')')
    print('Relationships Found: ' + str(len(res['inferred_relationships'])) + ' | ERD Connected: ' + str(res['schema_erd_connected']))
    print('ERD URL: ' + res['erd_diagram_url'])

if __name__ == '__main__':
    main()
