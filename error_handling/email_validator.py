class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MustContainOnlyOneAtSymbolError(Exception):  # If the given email contains more than one "@" symbol:
    pass


class NameTooLongError(Exception):  # If the length of the name is more than 20 characters.
    pass


class InvalidDomainNameError(Exception):  # If the name of the domain is not abv, hotmail, gmail, yahoo or outlook
    pass  # example: peter@gdhfsd.com


class InvalidDomainSeparatorError(Exception):  # If there is no '.' as a separator or if there are more
    pass                                       # then one '.' between the domain name and the domain.
    # example: peter@gmail..com, peter@gmailcom


allowed_domains = ['com', 'bg', 'org', 'net']
allowed_domain_names = ['hotmail', 'gmail', 'yahoo', 'outlook']

command = input()

while command != "End":

    try:
        if "@" not in command:
            raise MustContainAtSymbolError("Email must contain @")

        elif command.count("@") > 1:
            raise MustContainOnlyOneAtSymbolError("Email must contain only one '@' symbol.")

        elif len(command.split("@")[0]) <= 4:
            raise NameTooShortError("Name must be more than 4 characters")

        elif len(command.split("@")[0]) > 20:
            raise NameTooShortError("Name must be less than 20 characters")

        command = command.split("@")
        right_part_of_the_email = command[1]

        if ("." not in right_part_of_the_email or right_part_of_the_email.count(".") > 1) and right_part_of_the_email:
            raise InvalidDomainSeparatorError("The domain name and domain should be separated with '.'")

        elif right_part_of_the_email.split(".")[1] not in allowed_domains:
            raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

        elif right_part_of_the_email.split(".")[0] not in allowed_domain_names:
            raise InvalidDomainNameError("Domain name must be one of the following: hotmail, gmail, yahoo or outlook.")

    except IndexError:
        print("Invalid email!")

    else:
        print("Email is valid.")

    command = input()
