
def main():

	print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

	print("Initiating secure vault access...")

	with open("classified_data.txt", "r") as vault:
		print("Vault connection established with failsafe protocols\n")
		
		print("SECURE EXTRACTION:")
		vault_data = vault.read()
		print(vault_data)
	
	with open("security_protocols.txt", "r") as vault:

		vault_protocols = vault.read()

		print("\nSECURE PRESERVATION:")

		print(vault_protocols)
		
		print("Vault automatically sealed upon completion")

	with open("secure vault", "w") as  secure_vault:

		secure_vault.write(vault_data)
		secure_vault.write(f"\n{vault_protocols}")

	print("\nAll vault operations completed with maximum security.")


main()
