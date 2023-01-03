# Mikroservisa určená pre komunikáciue s databázou a GitLab serverom

Účel tejto mikroservisy je sprostredkúvať užívateľovi možnosť tvorby repozitáru na Gitlab servery, umožňuje vytvorenie repozitáru a pridávanie súborov. Tatiež mikroservisa spolupracuje so serverom na ktorom je spustená PostgreSQL databáza, v ktorej vytvára užívteľa a do tabulky ukladá jeho informácie + číslo jeho repozitáru, ktoré bude nasledne spracovávané ďaľšiou mikroservisou. 
