class ConfigData:

 TABLE_SCHEMA = '''
   
    {
  "hostId": "string",
  "pic": "int",
  "date": "string (YYYY-MM-DD)",

  "registerTS": "string (HH:MM:SS,ms)",
  "latestTS": "string (HH:MM:SS,ms)",
  "closedTS": "string (HH:MM:SS,ms)",

  "status": "string",   

  "identificationTS": "string (HH:MM:SS,ms)",
  "identification_location": "string",

  "exitTS": "string (HH:MM:SS,ms)",
  "exit_location": "string",

  "plc_number": "string",
  "Registered_location": "string",
  "customer_location": "string",
  "sort_strategy": "string",

  "barcode_data": {
    "barcodes": ["string"],
    "barcode_count": "int",
    "barcode_state": "int"
  },
  "barcode_error": "bool",

  "alibi_id": "string",

  "volume_data": {
    "volume_state": "int",
    "length": "int",
    "width": "int",
    "height": "int",
    "box_volume": "int",
    "real_volume": "int"
  },
  "volume_error": "bool",

  "item_state": "null | string",
  "actual_destination": "string",
  "destinations": ["string"],

  "destination_status": {
    "<destination_code>": "int"
  },

  "sort_code": "int",
  "entrance_state": "string | int",
  "exit_state": "null | string | int",
  "degister": "null | string",

  "events": [
    {
      
      "msg_id": "string | int",
      "type": "string",
      "location": "null | string",
      "raw": "string"
    }
  ]
}


 '''


 SCHEMA_DESCRIPTION = '''

   Key descriptions:

    1. HostId:
        - Unique ID from host system for parcel traceability.

    2. PIC:
        - Parcel ID assigned by area controller (not unique).

    3. Status:
        - Parcel processing state:
          - 'sorted': Successfully diverted.
          - 'unsorted': Sorting failed.
          - 'open': In progress.
          - 'sorted_off_end': Routed to default (no destination).

    4. Registered_location:
        - System location where scan/event occurred.

    5. customer_location:
        - Customer-defined logical location.

    6. sort_strategy:
        - Sorting method (e.g., 1 = original/alternative).
      

    7. destinations:
        - List of possible destination codes.

    8. barcode_data:
        - Scan info:
          - 'barcodes': List of codes.
          - 'barcode_count': Total read.
          - 'barcode_state': 6 = OK, else error.

    9. barcode_error:
        - True if 'barcode_state' ≠ 6.

    10. volume_data:
        - Volume scan info:
          - 'volume_state': 6 = OK, else error.
          - 'length', 'height', 'width'
          - 'real_volume', 'box_volume'

    11. volume_error_error:
        - True if 'volume_state' ≠ 6.

    12. alibi_id:
        - ID linking to volume scan event.

    13. actual_destination:
         this filed is not null if the status parcel get sorted then where it is actually sorted destination if it conatins 999 means parcel sorted but goes sorted_off_end.
        

    14. sort_code:
        - Sort result:
         this field is not null when item get sorted gives how the how sorted 1 mean good sort/ divert else some error is there.
          - 1 = Good sort; 
          other number indicates there is issue while sorting 
          if 1 mean Good sort
            this integre number
    15. exit_state:
        this filed is not null when item gets unsorted this gives reson why it does not sorted 
                          it values mapping are 1: lost
                                                2: end of tracking 
                                                3: handover

    16. events:
        this filed is used to captures the varoius events like item register,instruction type is stored in thta like item Register
        in raw filed there is acutal log for that
        if user askes to give me log just return raw filed.

'''


