import time
import click
import os


def format_time(seconds):
    minutes, seconds = divmod(seconds, 60)
    return '{:02d}:{:02d}'.format(minutes, seconds)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


@click.command()
@click.argument('study', type=int)
@click.argument('break_', type=int)

def pomodoro_timer(study, break_):
    click.echo('Pomodoro Timer')
    click.echo('Press Ctrl+C to exit')

    while True:
        try:
            clear_screen()
            click.echo('Work for {} minutes'.format(study))
            for remaining in range(study * 60, -1, -1):
                click.echo('\r{}'.format(format_time(remaining)), nl=False)
                time.sleep(1)

            clear_screen()
            click.echo('Take a break for {} minutes'.format(break_))
            for remaining in range(break_ * 60, -1, -1):
                click.echo('\r{}'.format(format_time(remaining)), nl=False)
                time.sleep(1)

        except KeyboardInterrupt:
            click.echo('\n\nExiting...')
            break


if __name__ == '__main__':
    pomodoro_timer()
