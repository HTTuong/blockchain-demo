class Node:
    def listen_for_input():
        while waiting_for_input:
            print('Please choose')
            print('1: Add a new transaction value')
            print('2: Mine a new block')
            print('3: Output the blockchain blocks')
            print('4: Check transaction validity')
            print('q: Quit')
            user_choice = get_user_choice()
            if user_choice == '1':
                tx_data = get_transaction_value()
                recipient, amount = tx_data
                # Add the transaction amount to the blockchain
                if add_transaction(recipient, amount=amount):
                    print('Added transaction!')
                else:
                    print('Transaction failed!')
                print(open_transactions)
            elif user_choice == '2':
                if mine_block():
                    open_transactions = []
                    save_data()
            elif user_choice == '3':
                print_blockchain_elements()
            elif user_choice == '4':
                verifier = Verification()
                if verifier.verify_transactions(open_transactions, get_balance):
                    print('All transactions are valid')
                else:
                    print('There are invalid transactions')
            elif user_choice == 'q':
                # This will lead to the loop to exist because it's running condition becomes False
                waiting_for_input = False
            else:
                print('Input was invalid, please pick a value from the list!')
            verifier = Verification()
            if not verifier.verify_chain(blockchain):
                print_blockchain_elements()
                print('Invalid blockchain!')
                # Break out of the loop
                break
            print('Balance of {}: {:6.2f}'.format('Max', get_balance('Max')))
        else:
            print('User left!')
    print('Done!')