class MultiTableSchemaForeignKeyInferrerClient:
    def infer_relational_schema(self, table_schemas=None):
        return {
            'inference_job_id': 'fky_inf_5519',
            'tables_analyzed': 4,
            'inferred_relationships': [
                {'from_table': 'orders', 'from_col': 'customer_id', 'to_table': 'customers', 'to_col': 'id', 'cardinality': 'MANY_TO_ONE'},
                {'from_table': 'order_items', 'from_col': 'order_id', 'to_table': 'orders', 'to_col': 'id', 'cardinality': 'MANY_TO_ONE'}
            ],
            'schema_erd_connected': True,
            'join_path_cache_valid': True,
            'erd_diagram_url': 'https://livedocs.erd.genpark.ai/schemas/5519.json'
        }
