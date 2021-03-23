form = [
  {
    "name": "table_name", 
    "label": "Table Name",
    "description": "Defaults to report name if left blank", 
    "type":"string", 
    "required": False, 
    "sensitive": True
  },
  {
    "name": "insert_mode", 
    "label": "Select Insert Mode", 
    "type":"select",
    "required": True, 
    "sensitive": False, 
    "options": [
      {
        "name": "append",
        "label": "Append Data"
      },
      {
        "name": "upsert", 
        "label": "Update and Insert Data"
      },
      {
        "name": "new", 
        "label": "Create New Table"
      }
    ]
  }
]