import journaling
import summary

def main():
    while True:
        choice = input("\n Journaling (1) \n Plot (2)\n")

        if choice == "1":
            journaling.proccessResponses()
            journaling.saveResponsesToFile()
        elif choice == "2":
            # Ask the user for multiple plot choices
            print("\nWhich plot(s) do you want to generate?")
            print("1. Bar plot of average sentiment scores by category")
            print("2. Line plot of average compound score over time")
            print("3. Exit plot menu")

            plot_choices = input("Enter the numbers of the plots you want (e.g., 1 2):\n").split()

            # Load data from files once, to avoid reloading for each plot
            data = summary.load_responses_from_files()
            
            # Loop through choices and generate the corresponding plots
            for plot_choice in plot_choices:
                if plot_choice == "1":
                    summary.plot_summary(data, plot_type="bar")
                elif plot_choice == "2":
                    summary.plot_summary(data, plot_type="line")
                elif plot_choice == "3":
                    print("Exiting plot menu...")
                    break  # Exit plot menu loop
                else:
                    print(f"Invalid choice: {plot_choice}. Please choose 1, 2, or 3.")
        else:
            print("Exiting...")
            break  # Exit the main loop

if __name__ == "__main__":
    main()
