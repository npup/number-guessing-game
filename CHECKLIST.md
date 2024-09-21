# Checkpoints

## 1. Player name (2 points)

Name should be a string of characters only (no numbers) and one whitespace only between first name and last name.

> Kolla:  
> Ingen kombination av space/tab osv. fungerar om de är fler än två  
> Man måste ange två ord - inte ett eller tre eller annat antal  
> Inget av orden får innehålla annat än bokstäver (men åäöèñû etc går bra).

## 2. Birthdate as yyyymmdd (3 points)

Validate input to be:

-   a year after 1900 in yyyy
-   a valid date in general

> Kolla:  
> Man får inte ange datum som "inte finns" (94 maj, 30 februari osv)  
> Årtalet måste vara större än 1900

## 3. Player age (3 points)

Calculates the player age from the birthdate

> Kolla:  
> Åldern räknas ut med avseende på dagens datum  
>  (dvs. man räknas som 18 om man fyller senast "idag").

## 4. Player age validation (2 points)

-   Player age must be at least 18
-   If not, user is asked to enter age again (step 2)

> Kolla:  
> Alla åldrar under 18 år avseende dagens datum nekas att spela.

## 5. Create a list containing random numbers (5 points)

    -   numbers are between 0 and 100 (inclusive)
    -   numbers are unique within the list
    -   numbers are sorted in ascending order, from left to right

> Kolla:  
> Listan är 10 siffror  
> Listan har aldrig nummer mindre än 0 eller högre än 100  
> Listan har inga nummer som repeteras  
> Listan är sorterad i stigande ordning

## 6. Create a secret number for player to guess (5 points)

One of the numbers in the list is (randomly) identified as the secret (lucky) number.

> Kolla:  
> Det finns ett visst nummer som är "hemlisen".  
> (det skrivs ut på skärmen när spelet startar om man har slagit på DEBUG = True i settingsfilen).

## 7. Prints the list of numbers and ask player to guess (5 points)

The guessed number is saved for comparisons.

> Kolla:  
> Listan skrivs ut i sin helhet.  
> Det går inte att se på den vilket som är det hemliga numret.

## 8. On player making correct choice (5 points)

-   Game prints: "Congratulations, game is over." and the number of attempts used.
-   The player is prompted to play again (y/n).
-   If y (yes) game restarts from step 5.
-   If n (no) game exits.

> Kolla:  
> Antalet försök som rapporteras skall stämma med hur många gånger man faktiskt gissat.  
> y/n-valet skall fungera

## On player NOT making correct choice

### 9. Handle wrong guess (5 points)

Create a new list from the current one, by removing any number NOT within 10
from the secret (lucky) number.

> Kolla:  
> Listan skall i denna operation plocka bort nummer som är utanför det tillåtna området.

### 10. Print new list with and prompt to guess again (5 points)

1. Game deletes the guessed number number from the list

If the list is "too short" (2 items or less) game is over with a failure message. Else:

2.  Print the list
3.  With the prompt, an attemps count is also shown.

> Kolla:  
> Listan skall sakna det senast felaktigt gissade numret.  
> Om listan blivit för kort skrivs ett meddelande ut på skärmen om det innan spelet avslutas.

### 11. On player making correct choice in the new list (5 points)

Game is over (execute step 8).

### 12. On player making incorrect choice (5 points)

    - Go to step 10 (print list and guess again)
