folder architectures


      apis/v1:
            config:
              - db_config.py
              - es_config.py
            app1:
              routers:
              - user_routes.py
              - employees_routes.py
        
              services:
               - users_services.py    # for business logic or database related logic app related helpers.
               - employee_services.py
      
               models:
                 user_models.py
                 employee_models.py
      
              schemas:
                - user_schema.py
                - employee_schema.py
      
            utils:
              global_helper.py  # like string manipulations and etc.
      
            middlewares:
              - error_handler.py
      
            custom_exception:
              - custom_error.py

            tests:
              app1:
                user_test_case.py
        
            main.py
            config.py
      
         
      
