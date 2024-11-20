# Class to represent a Certificate
class Certificate:
    def __init__(self, issuer, subject, data):
        """
        Initialize a certificate with the following details:
        :param issuer: The entity or CA issuing the certificate
        :param subject: The entity or CA receiving the certificate
        :param data: Information or details of the certificate
        """
        self.issuer = issuer
        self.subject = subject
        self.data = data

    def __repr__(self):
        """
        String representation of the certificate for easy display.
        """
        return f"Certificate(issuer={self.issuer}, subject={self.subject}, data={self.data})"


# Class to represent an Entity (e.g., A, C, M1, M2)
class Entity:
    def __init__(self, name):
        """
        Initialize an entity with a name and an empty list of received certificates.
        :param name: Name of the entity (e.g., A, C, M1, M2)
        """
        self.name = name  # Name of the entity
        self.received_certificates = []  # List to hold received certificates

    def receive_certificate(self, certificate):
        """
        Receive a certificate and store it in the entity's received certificates list.
        :param certificate: The Certificate object to store
        """
        self.received_certificates.append(certificate)

    def __repr__(self):
        """
        String representation showing the entity and its received certificates.
        """
        return f"Entity(name={self.name}, received={self.received_certificates})"


# Class to represent a Certificate Authority (CA)
class CertificateAuthority(Entity):
    def __init__(self, name):
        """
        Initialize a CA with a name, inherited as an entity, 
        and an additional list for issued certificates.
        :param name: Name of the Certificate Authority (e.g., B, D, E, F)
        """
        super().__init__(name)  # Initialize as an entity
        self.issued_certificates = []  # List to hold issued certificates

    def issue_certificate(self, subject, data):
        """
        Issue a certificate to a subject.
        :param subject: The entity or CA receiving the certificate
        :param data: Details or content of the certificate
        :return: The issued Certificate object
        """
        certificate = Certificate(issuer=self.name, subject=subject.name, data=data)
        self.issued_certificates.append(certificate)  # Store in forward certificates
        subject.receive_certificate(certificate)  # Send to subject
        return certificate

    def get_forward_certificates(self):
        """
        Retrieve all forward certificates (certificates this CA issued).
        :return: List of issued certificates
        """
        return self.issued_certificates

    def get_reverse_certificates(self):
        """
        Retrieve all reverse certificates (certificates this CA received).
        :return: List of received certificates
        """
        return self.received_certificates


# Initialize Entities (A, C, M1, M2) and Certificate Authorities (B, D, E, F)
a = Entity('A')
b = CertificateAuthority('B')
c = Entity('C')
d = CertificateAuthority('D')
e = CertificateAuthority('E')
f = CertificateAuthority('F')
m1 = Entity('M1')
m2 = Entity('M2')

# Issuing certificates from Certificate Authority B
b.issue_certificate(a, "Cert B->A")  # B issues a certificate to A
b.issue_certificate(d, "Cert B->D")  # B issues a certificate to D
b.issue_certificate(c, "Cert B->C")  # B issues a certificate to C

# Issuing certificates from Certificate Authority D
d.issue_certificate(e, "Cert D->E")  # D issues a certificate to E
d.issue_certificate(b, "Cert D->B")  # D issues a certificate to B
d.issue_certificate(f, "Cert D->F")  # D issues a certificate to F

# Issuing certificates from Certificate Authority E
e.issue_certificate(d, "Cert E->D")  # E issues a certificate to D
e.issue_certificate(f, "Cert E->F")  # E issues a certificate to F

# Issuing certificates from Certificate Authority F
f.issue_certificate(m2, "Cert F->M2")  # F issues a certificate to M2

# Directly receive certificates
a.receive_certificate(Certificate('A', m1.name, "Cert A->M1"))  # A receives a certificate from M1

# Reverse Certificates
e.receive_certificate(d.issue_certificate(f, "Cert D->F"))  # D issues a certificate to F; F receives it
b.receive_certificate(d.issue_certificate(b, "Cert D->B"))  # D issues a certificate to B; B receives it

# Display Forward Certificates (Certificates issued by each CA)
print("Forward Certificates from CA B:")
print(b.get_forward_certificates())

print("\nForward Certificates from CA D:")
print(d.get_forward_certificates())

print("\nForward Certificates from CA E:")
print(e.get_forward_certificates())

print("\nForward Certificates from CA F:")
print(f.get_forward_certificates())

# Display Reverse Certificates (Certificates received by each CA)
print("\nReverse Certificates for CA E:")
print(e.get_reverse_certificates())

print("\nReverse Certificates for CA B:")
print(b.get_reverse_certificates())
