from db_manager import HeroDatabase
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()

def main():
    db = HeroDatabase()

    while True:
        menu_content = (
            "[bold cyan]1.[/] Add New Hero\n"
            "[bold cyan]2.[/] View All Heroes\n"
            "[bold cyan]3.[/] Update Hero\n"
            "[bold cyan]4.[/] Delete Hero\n"
            "[bold red]5.[/] Exit"
        )

        console.print(Panel(
            menu_content,
            title="🛡️  GUILD MANAGER",
            subtitle="Choose an action",
            style="bold blue",
            width=50
        ))

        choice = Prompt.ask("👉 What connects your destiny?", choices=["1", "2", "3", "4", "5"])

        if choice == "1":
            console.rule("[bold green]➕ Add New Hero[/]")

            name = Prompt.ask("Name")
            role = Prompt.ask("Class/Role", default="Warrior")
            level = int(Prompt.ask("Level", default="1"))
            gold = int(Prompt.ask("Gold", default="0"))

            is_alive_str = Prompt.ask("Is Alive?", choices=["y", "n"], default="y")
            is_alive = True if is_alive_str == "y" else False

            db.add_hero(name, role, level, gold, is_alive)
            console.print(f"[bold green]✅ {name} has joined the guild![/]")

        elif choice == '2':
            heroes = db.get_heroes()

            if not heroes:
                console.print("[yellow] ⚠️  The guild is empty![/]")
            else:
                table = Table(title="📋 Guild Members", show_header=True, header_style="bold magenta")

                table.add_column("ID", style="cyan", justify="center")
                table.add_column("Name", style="green")
                table.add_column("Role", style="blue")
                table.add_column("Lvl", justify="right")
                table.add_column("Gold", justify="right", style="gold1")
                table.add_column("Status", justify="center")

                for hero in heroes:
                    status_icon = "❤️" if hero[5] else "💀"
                    
                    table.add_row(
                        str(hero[0]), 
                        hero[1], 
                        hero[2], 
                        str(hero[3]), 
                        f"{hero[4]} 💰", 
                        status_icon
                    )
                
                console.print(table)
            
            Prompt.ask("\nPress Enter to continue")

        elif choice == '3':
            console.rule("[bold yellow]⚡ Update Hero[/]")
            hero_id = int(Prompt.ask("ID of the hero to update"))
            new_lvl = int(Prompt.ask("New Level"))
            new_gold = int(Prompt.ask("New Gold Amount"))
            
            db.update_hero(hero_id, new_lvl, new_gold)

        elif choice == '4':
            console.rule("[bold red]🗑️  Delete Hero[/]")
            hero_id = int(Prompt.ask("ID of the hero to DELETE"))
            
            # Uma confirmação de segurança
            confirm = Prompt.ask(f"Are you sure you want to delete ID {hero_id}?", choices=["y", "n"])
            if confirm == "y":
                db.delete_hero(hero_id)
            else:
                console.print("[dim]Operation cancelled.[/]")    

        elif choice == '5':
            console.print("[bold blue]👋 Closing the Guild gate... See you![/]")
            db.close_connection()
            break

if __name__ == "__main__":
    main()