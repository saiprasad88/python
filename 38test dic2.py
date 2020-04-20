monthconversions ={"jan": "january",
                    "feb": "febuary",
                    "mar": "march",
                    "apr": "april",
                    "may": "may",
                    "jun": "june",
                    "jul": "july",
                    "aug": "august",
                    "sep": "september",
                    "nov": "november",
                    "oct": "october",
                    "dec": "december",
                   }
print(monthconversions.get("dec"))
print(monthconversions.get("luv","not a valid key"))
print(monthconversions.get("ggg"))