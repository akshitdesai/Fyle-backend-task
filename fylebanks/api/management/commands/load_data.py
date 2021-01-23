from django.core.management.base import BaseCommand, CommandError
from api.models import Bank, Branch
from csv import DictReader

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('file_name', nargs='?', type=str)

    def handle(self, *args, **options):
        file_name = options['file_name']
        try:
            with open(file_name, 'r') as read_obj:
                csv_dict_reader = DictReader(read_obj)
                self.stdout.write(self.style.SQL_TABLE("\nSaving data to Branch table"))
                
                banks = set()
                i = 0
                sucess = 0
                failed = 0
                for row in csv_dict_reader:
                    new_branch = Branch(
                        ifsc = row.get('ifsc'),
                        bank_id = row.get('bank_id'),
                        branch = row.get('branch'),
                        address = row.get('address'),
                        city = row.get('city'),
                        district = row.get('district'),
                        state = row.get('state')
                    )
                    new_bank = Bank(
                        id = row.get('bank_id'),
                        name = row.get('bank_name')
                    )
                    banks.add(new_bank)
                    i += 1
                    print(i, end=' ')
                    try:
                        new_branch.save()
                        sucess += 1
                    except Exception as error:
                        failed += 1
                if sucess:
                    self.stdout.write(self.style.SUCCESS(f"Completed!✅ {sucess} rows saved"))
                if failed:
                    self.stdout.write(self.style.WARNING(f"Failed!❌ {failed} rows failed to save"))

                        
                self.stdout.write(self.style.SQL_TABLE("\nSaving data to Bank table"))
                sucess = 0
                failed = 0
                for bank in banks:
                    try:
                        bank.save()
                        sucess += 1
                    except Exception as error:
                        failed += 1
                if sucess:
                    self.stdout.write(self.style.SUCCESS(f"Completed!✅ {sucess} rows saved"))
                if failed:
                    self.stdout.write(self.style.WARNING(f"Failed!❌ {failed} rows failed to save"))

        except Exception as error:
            self.stdout.write(self.style.ERROR("\nFailed to save data ❌\n"))

