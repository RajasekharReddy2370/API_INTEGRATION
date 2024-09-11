from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests

import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class place_order_t(APIView):
    def post(self, request):
        try:
            payload = request.data
            url = "https://robotapitest-in.borzodelivery.com/api/business/1.6/create-order"
            headers = {
                'X-DV-Auth-Token': '370561FC3C82DB38C83E65467A8D2429CC3D8E75',
                'Content-Type': 'application/json'
            }
            response = requests.post(url, headers=headers, json=payload)
            response.raise_for_status()  # Will raise an HTTPError for bad responses
            response_data = response.json()
            result = {
                "is_successful": response_data.get("is_successful"),
                "order": {}
            }
            if response_data.get("order"):
                order = response_data["order"]
                result["order"] = {
                    "order_id": order.get("order_id"),
                    "payment_amount": order.get("payment_amount"),
                    "points": []
                }
                for point in order.get("points", []):
                    point_details = {
                        "address": point.get("address"),
                        "contact_person": {
                            "name": point.get("contact_person", {}).get("name"),
                            "phone": point.get("contact_person", {}).get("phone")
                        },
                        "tracking_url": point.get("tracking_url"),
                    }
                    result["order"]["points"].append(point_details)
            return Response(result, status=status.HTTP_200_OK)
        except requests.exceptions.RequestException as e:
            # Handle any errors with the request to the external API
            return Response({"error": str(e)}, status=status.HTTP_502_BAD_GATEWAY)
        except Exception as e:
            # Handle any other exceptions
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class place_order_p(APIView):
    def post(self, request):
        try:
            payload = request.data
            url = "https://robot-in.borzodelivery.com/api/business/1.6/create-order"
            headers = {
                'X-DV-Auth-Token': '9B4A84BBEC57ED51BED5C8D44E06BF4ED9C0FDD4',
                'Content-Type': 'application/json'
            }
            response = requests.post(url, headers=headers, json=payload)
            response.raise_for_status()  # Will raise an HTTPError for bad responses
            response_data = response.json()
            result = {
                "is_successful": response_data.get("is_successful"),
                "order": {}
            }
            if response_data.get("order"):
                order = response_data["order"]
                result["order"] = {
                    "order_id": order.get("order_id"),
                    "payment_amount": order.get("payment_amount"),
                    "points": []
                }
                for point in order.get("points", []):
                    point_details = {
                        "address": point.get("address"),
                        "contact_person": {
                            "name": point.get("contact_person", {}).get("name"),
                            "phone": point.get("contact_person", {}).get("phone")
                        },
                        "tracking_url": point.get("tracking_url"),
                    }
                    result["order"]["points"].append(point_details)
            return Response(result, status=status.HTTP_200_OK)
        except requests.exceptions.RequestException as e:
            # Handle any errors with the request to the external API
            return Response({"error": str(e)}, status=status.HTTP_502_BAD_GATEWAY)
        except Exception as e:
            # Handle any other exceptions
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class price(APIView):
    def post(self,request):
        try:
            payload = request.data
            url = "https://robotapitest-in.borzodelivery.com/api/business/1.6/calculate-order"
            headers = {
                'X-DV-Auth-Token': '370561FC3C82DB38C83E65467A8D2429CC3D8E75',
                'Content-Type': 'application/json'
            }
            response = requests.post(url, headers=headers, json=payload)
            response_data = response.json()
            result = {
                "is_successful": response_data.get("is_successful"),
                "order": {}
            }
            if response_data.get("order"):
                order = response_data["order"]
                result["order"] = {
                    "order_id": order.get("order_id"),
                    "payment_amount": order.get("payment_amount"),
                    "points": []
                }
                for point in order.get("points", []):
                    point_details = {
                        "address": point.get("address"),
                        "contact_person": {
                            "name": point.get("contact_person", {}).get("name"),
                            "phone": point.get("contact_person", {}).get("phone")
                        },
                        # "tracking_url": point.get("tracking_url"),
                    }
                    result["order"]["points"].append(point_details)
            return Response(result, status=status.HTTP_200_OK)
        except requests.exceptions.RequestException as e:
            # Handle any errors with the request to the external API
            return Response({"error": str(e)}, status=status.HTTP_502_BAD_GATEWAY)
        except Exception as e:
            # Handle any other exceptions
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class Edit_order_p(APIView):
    def post(self,request):
        try:
            payload = request.data
            url = "https://robot-in.borzodelivery.com/api/business/1.6/edit-order"
            headers = {
                'X-DV-Auth-Token': '9B4A84BBEC57ED51BED5C8D44E06BF4ED9C0FDD4',
                'Content-Type': 'application/json'
            }
            response = requests.post(url, headers=headers, json=payload)
            response.raise_for_status()  # Will raise an HTTPError for bad responses
            response_data = response.json()
            result = {
                "is_successful": response_data.get("is_successful"),
                "order": {}
            }
            if response_data.get("order"):
                order = response_data["order"]
                result["order"] = {
                    "order_id": order.get("order_id"),
                    "payment_amount": order.get("payment_amount"),
                    "points": []
                }
                for point in order.get("points", []):
                    point_details = {
                        "address": point.get("address"),
                        "contact_person": {
                            "name": point.get("contact_person", {}).get("name"),
                            "phone": point.get("contact_person", {}).get("phone")
                        },
                        "tracking_url": point.get("tracking_url"),
                    }
                    result["order"]["points"].append(point_details)
            return Response(result, status=status.HTTP_200_OK)
        except requests.exceptions.RequestException as e:
            # Handle any errors with the request to the external API
            return Response({"error": str(e)}, status=status.HTTP_502_BAD_GATEWAY)
        except Exception as e:
            # Handle any other exceptions
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class Edit_order_t(APIView):
    def post(self,request):
        try:
            payload = request.data
            url = "https://robotapitest-in.borzodelivery.com/api/business/1.6/edit-order"
            headers = {
                'X-DV-Auth-Token': '370561FC3C82DB38C83E65467A8D2429CC3D8E75',
                'Content-Type': 'application/json'
            }
            response = requests.post(url, headers=headers, json=payload)
            response.raise_for_status()  # Will raise an HTTPError for bad responses
            response_data = response.json()
            result = {
                "is_successful": response_data.get("is_successful"),
                "order": {}
            }
            if response_data.get("order"):
                order = response_data["order"]
                result["order"] = {
                    "order_id": order.get("order_id"),
                    "payment_amount": order.get("payment_amount"),
                    "points": []
                }
                for point in order.get("points", []):
                    point_details = {
                        "address": point.get("address"),
                        "contact_person": {
                            "name": point.get("contact_person", {}).get("name"),
                            "phone": point.get("contact_person", {}).get("phone")
                        },
                        "tracking_url": point.get("tracking_url"),
                    }
                    result["order"]["points"].append(point_details)
            return Response(result, status=status.HTTP_200_OK)
        except requests.exceptions.RequestException as e:
            # Handle any errors with the request to the external API
            return Response({"error": str(e)}, status=status.HTTP_502_BAD_GATEWAY)
        except Exception as e:
            # Handle any other exceptions
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# class place_order_t(APIView):
#     def post(self, request):
#         try:
#             # Extract data from the request
#             matter = request.data.get("matter")
#             order_type = request.data.get("type")
#             total_weight_kg = request.data.get("total_weight_kg")
#             points = request.data.get("points", [])
#
#
#             # Define the URL and headers for the API call
#             # TEST
#             url = "https://robotapitest-in.borzodelivery.com/api/business/1.6/create-order"
#             # PROD
#             # url = "https://robot-in.borzodelivery.com/api/business/1.6/create-order"
#
#             headers = {
#                 # TEST
#                 'X-DV-Auth-Token': '370561FC3C82DB38C83E65467A8D2429CC3D8E75',
#                 # PROD
#                 # 'X-DV-Auth-Token': '9B4A84BBEC57ED51BED5C8D44E06BF4ED9C0FDD4',
#                 'Content-Type': 'application/json'
#             }
#
#             # Prepare the payload with dynamic values
#             payload = {
#                 "matter": matter,
#                 "type": order_type,
#                 "total_weight_kg": total_weight_kg,
#                 "points": points,
#             }
#
#             # Perform the HTTP POST request to the external API
#             response = requests.post(url, headers=headers, json=payload)
#
#             # Convert the response to JSON format
#             response_data = response.json()
#
#             # Extract relevant fields from the response
#             result = {
#                 "is_successful": response_data.get("is_successful"),
#                 "order": {}
#             }
#
#             if response_data.get("order"):
#                 order = response_data["order"]
#                 result["order"] = {
#                     "order_id": order.get("order_id"),
#                     "payment_amount": order.get("payment_amount"),
#                     "points": []
#                 }
#
#                 for point in order.get("points", []):
#                     point_details = {
#                         "address": point.get("address"),
#                         "contact_person": {
#                             "name": point.get("contact_person", {}).get("name"),
#                             "phone": point.get("contact_person", {}).get("phone")
#                         },
#                         "tracking_url": point.get("tracking_url"),
#                     }
#                     result["order"]["points"].append(point_details)
#
#                 # Return the structured response
#                 return Response(result, status=status.HTTP_200_OK)
#
#         except requests.exceptions.RequestException as e:
#             # Handle any errors with the request to the external API
#             return Response({"error": str(e)}, status=status.HTTP_502_BAD_GATEWAY)
#
#         except Exception as e:
#             # Handle any other exceptions
#             return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# class place_order_p(APIView):
#     # Restrict the view to handle only POST requests
#     # http_method_names = ['post']
#     def post(self, request):
#         try:
#             # Extract data from the request
#             matter = request.data.get("matter")
#             order_type = request.data.get("type")
#             total_weight_kg = request.data.get("total_weight_kg")
#             points = request.data.get("points", [])
#             payment_method = request.data.get("payment_method")
#
#
#             # Define the URL and headers for the API call
#             # TEST
#             # url = "https://robotapitest-in.borzodelivery.com/api/business/1.6/create-order"
#             # PROD
#             url = "https://robot-in.borzodelivery.com/api/business/1.6/create-order"
#
#             headers = {
#                 # TEST
#                 # 'X-DV-Auth-Token': '370561FC3C82DB38C83E65467A8D2429CC3D8E75',
#                 # PROD
#                 'X-DV-Auth-Token': '9B4A84BBEC57ED51BED5C8D44E06BF4ED9C0FDD4',
#                 'Content-Type': 'application/json'
#             }
#
#             # Prepare the payload with dynamic values
#             payload = {
#                 "matter": matter,
#                 "type": order_type,
#                 "total_weight_kg": total_weight_kg,
#                 "points": points,
#                 "payment_method":payment_method
#             }
#
#             # Perform the HTTP POST request to the external API
#             response = requests.post(url, headers=headers, json=payload)
#
#             # Convert the response to JSON format
#             response_data = response.json()
#
#             # Extract relevant fields from the response
#             result = {
#                 "is_successful": response_data.get("is_successful"),
#                 "order": {}
#             }
#
#             if response_data.get("order"):
#                 order = response_data["order"]
#                 result["order"] = {
#                     "order_id": order.get("order_id"),
#                     "payment_amount": order.get("payment_amount"),
#                     "points": []
#                 }
#
#                 for point in order.get("points", []):
#                     point_details = {
#                         "address": point.get("address"),
#                         "contact_person": {
#                             "name": point.get("contact_person", {}).get("name"),
#                             "phone": point.get("contact_person", {}).get("phone")
#                         },
#                         "tracking_url": point.get("tracking_url"),
#                     }
#                     result["order"]["points"].append(point_details)
#
#                 # Return the structured response
#                 return Response(result, status=status.HTTP_200_OK)
#
#         except requests.exceptions.RequestException as e:
#             # Handle any errors with the request to the external API
#             return Response({"error": str(e)}, status=status.HTTP_502_BAD_GATEWAY)
#
#         except Exception as e:
#             # Handle any other exceptions
#             return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# class price(APIView):
#     def post(self,request):
#         try:
#             # Extract data from the request
#             matter = request.data.get("matter")
#             order_type = request.data.get("type")
#             total_weight_kg = request.data.get("total_weight_kg")
#             points = request.data.get("points", [])
#
#             # Define the URL and headers for the API call
#             url = "https://robotapitest-in.borzodelivery.com/api/business/1.6/calculate-order"
#             headers = {
#                 'X-DV-Auth-Token': '370561FC3C82DB38C83E65467A8D2429CC3D8E75',
#                 'Content-Type': 'application/json'
#             }
#
#             # Prepare the payload with dynamic values
#             payload = {
#                 "matter": matter,
#                 "type": order_type,
#                 "total_weight_kg": total_weight_kg,
#                 "points": points
#             }
#
#             # Perform the HTTP POST request to the external API
#             response = requests.post(url, headers=headers, json=payload)
#
#             # Convert the response to JSON format
#             response_data = response.json()
#
#             # Extract relevant fields from the response
#             result = {
#                 "is_successful": response_data.get("is_successful"),
#                 "order": {}
#             }
#
#             if response_data.get("order"):
#                 order = response_data["order"]
#                 result["order"] = {
#                     "order_id": order.get("order_id"),
#                     "payment_amount": order.get("payment_amount"),
#                     "points": []
#                 }
#
#                 for point in order.get("points", []):
#                     point_details = {
#                         "address": point.get("address"),
#                         "contact_person": {
#                             "name": point.get("contact_person", {}).get("name"),
#                             "phone": point.get("contact_person", {}).get("phone")
#                         },
#                         # "tracking_url": point.get("tracking_url"),
#                     }
#                     result["order"]["points"].append(point_details)
#
#             # Return the structured response
#             return Response(result, status=status.HTTP_200_OK)
#
#         except requests.exceptions.RequestException as e:
#             # Handle any errors with the request to the external API
#             return Response({"error": str(e)}, status=status.HTTP_502_BAD_GATEWAY)
#
#         except Exception as e:
#             # Handle any other exceptions
#             return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


########################################################## STATIC PAYLOAD #######################################################
# from django.http import HttpResponse, JsonResponse
# from django.shortcuts import render
# import requests
# import requests
# from django.http import JsonResponse
#
# def create_order(request):
#     # Define the URL and headers
#     url = "https://robotapitest-in.borzodelivery.com/api/business/1.6/create-order"
#     headers = {
#         'X-DV-Auth-Token': '370561FC3C82DB38C83E65467A8D2429CC3D8E75',
#         'Content-Type': 'application/json'
#     }
#
#     # Define the data payload
#     data = {
#         "matter": "electronics",
#         "type": "standard",
#         "total_weight_kg": 6,
#         "points": [
#             {
#                 "address": "Saket, New Delhi, Delhi 110017, India",
#                 "contact_person": {"name": "raja", "phone": "911234567890"}
#             },
#             {
#                 "address": "Janakpuri, New Delhi, Delhi, India",
#                 "contact_person": {"name": "chen", "phone": "919876543210"}
#             }
#         ]
#     }
#
#     # Perform the HTTP POST request
#     response = requests.post(url, headers=headers, json=data)
#
#     # Convert the response to JSON format
#     response_data = response.json()
#
#     # Extract relevant fields from the response
#     result = {
#         "is_successful": response_data.get("is_successful"),
#         "order": {}
#     }
#
#     if response_data.get("order"):
#         order = response_data["order"]
#         result["order"] = {
#             "order_id": order.get("order_id"),
#             "payment_amount": order.get("payment_amount"),
#
#             "points": []
#         }
#
#         for point in order.get("points", []):
#             point_details = {
#                 "address": point.get("address"),
#                 "contact_person": {
#                     "name": point.get("contact_person", {}).get("name"),
#                     "phone": point.get("contact_person", {}).get("phone")
#                 },
#                 "tracking_url": point.get("tracking_url"),
#             }
#
#             result["order"]["points"].append(point_details)
#
#     # Return the filtered JSON data as a JsonResponse
#     return JsonResponse(result, json_dumps_params={'indent': 4})

############################################################## BLOW HORN ######################################

class CreateOrderBlowhorn(APIView):
    def post(self, request):
        url = "https://beta.blowhorn.com/api/orders/list"

        headers = {
            'API_KEY': 'tqF4zGyJAfa7W6d1bP2Y0BpXRjwe3o',
            'Content-Type': 'application/json'
        }

        data = {
    "pickup_time": {
    "type": "later",
    "value": "2024-09-03T18:41:00.408907"
    },
    "pickup": {
    "name": "Home",
    "address": {
      "area": "HSR Layout",
      "city": "Bengaluru",
      "postal_code": 560095,
      "full_address": "245, 2nd Cross, HSR Layout Bengaluru"
    },
    "contact": {
      "name": "Mahadevappa",
      "mobile": 9999999999
    },
    "geopoint": {
      "lat": 12.9081357,
      "lng": 77.64760799999999
    }
    },
    "dropoff": {
    "name": "Work",
    "address": {
      "area": "BTM Layout",
      "city": "Bengaluru",
      "postal_code": 560034,
      "full_address": "245, 3rd Main, BTM Layout Bengaluru"
    },
    "contact": {
      "name": "Raj",
      "mobile": 9849314733
    },
    "geopoint": {
      "lat": 12.9165757,
      "lng": 77.61011630000007
    }
    },
    "waypoints": [
    {
      "sequence_id": "1",
      "name": "Waypoint 1",
      "address": {
        "area": "HSR Layout",
        "city": "Bengaluru",
        "postal_code": 560102,
        "full_address": "2287 16th Cross Rd Vanganahalli 1st Sector HSR Layout Bengaluru 560102"
      },
      "contact": {
        "name": "Puneet",
        "mobile": 9701488435
      },
      "geopoint": {
        "lat": 12.912442595996774,
        "lng": 77.64740069737547
      }
    }
    ],
    "items": [
    "Chair",
    "Table"
    ],
    "num_of_labours": 1,
    "vehicle_class": "Mini-Truck",
    "payment_mode": "Online",
    "price_type": "full-day"
    }
        response = requests.post(url, headers=headers, json=data)

        print(response.text)


#         try:
#             # Extract data from the request
#             data = request.data
#
#             # Define the URL and headers
#             url = "https://beta.blowhorn.com/api/orders/booking"
#             headers = {
#                 'API_KEY': 'tqF4zGyJAfa7W6d1bP2Y0BpXRjwe3o',
#                 'Content-Type': 'application/json'
#             }
#
#             # Perform the HTTP POST request
#             response = requests.post(url, headers=headers, json=data)
#
#             # Convert the response to JSON format
#             response_data = response.json()
#
#             # Return the response data
#             return JsonResponse(response_data, json_dumps_params={'indent': 4})
#
#         except requests.exceptions.RequestException as e:
#             # Handle any errors with the request to the external API
#             return JsonResponse({"error": str(e)}, status=502)
#
#         except Exception as e:
#             # Handle any other exceptions
#             return JsonResponse({"error": str(e)}, status=500)

# import logging
# import requests
#
# from django.http import JsonResponse
# from django.views.decorators.http import require_POST
# from rest_framework.views import APIView
#
# logger = logging.getLogger(__name__)
#
# class CreateOrderBlowhorn(APIView):
#     @require_POST
#     def post(self, request):
#         try:
#             # Extract data from the request
#             data = request.data
#
#             # Validate the data
#             if not validate_data(data):
#                 return JsonResponse({"error": "Invalid data"}, status=400)
#
#             # Define the URL and headers
#             url = "https://beta.blowhorn.com/api/orders/booking"
#             headers = {
#                 'API_KEY': 'tqF4zGyJAfa7W6d1bP2Y0BpXRjwe3o',
#                 'Content-Type': 'application/json'
#             }
#
#             # Perform the HTTP POST request
#             response = requests.post(url, headers=headers, json=data)
#             logger.info(f"Request sent to Blowhorn: {response.url}")
#
#             # Check for HTTP errors
#             response.raise_for_status()
#
#             # Convert the response to JSON format
#             response_data = response.json()
#
#             # Format the response into the desired structure
#             # result = {
#             #     "status": "PASS",
#             #     "message": {
#             #         "order_number": response_data.get("order_number"),
#             #         "tracking_url": response_data.get("tracking_url"),
#             #         "estimated_distance": response_data.get("estimated_distance"),
#             #         "estimated_cost": response_data.get("estimated_cost")
#             #     }
#             # }
#
#             # Return the formatted response
#             return JsonResponse(response, json_dumps_params={'indent': 4})
#
#         except requests.exceptions.HTTPError as e:
#             logger.error(f"Error from Blowhorn API: {e}")
#             return JsonResponse({"error": str(e)}, status=502)
#
#         except Exception as e:
#             logger.exception("Unexpected error:")
#             return JsonResponse({"error": str(e)}, status=500)
#
# def validate_data(data):
#     # Implement your data validation logic here
#     # For example, check for required fields, data types, and ranges
#     return True
