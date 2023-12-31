# Voting on Superheroes Questionnaire : Project Overview

![Voting on a Poll](assets/img/poll.jpg)

## Background
In this personal project, I studied the computational aspects of different voting methods. The prevalent philosophy about voting in the United States (and in the Western world in general) is the one person, one vote principle. Under this system, every voter casts a ballot supporting their preferred candidate, and the candidate with the most votes wins. This method is known as plurality voting. While it may seem like a common-sense approach, it is the source of much unfairness in election results. The most common problem with plurality voting is the phenomenon of vote splitting, in which multiple candidates run on similar platforms and each gets a share of (thereby "splitting") the same electorate. When this happens, a candidate disliked by the majority of the population can still win an election simply because the vote against them is split.
In the US, the most familiar form of vote splitting is the spoiler effect, in which a third candidate draws a significant share of the votes from either the Democrat or the Republican that would have otherwise won. The 1992 victory of Bill Clinton over George H.W. Bush was the result of (Republican) vote splitting by the spoiler candidate Ross Perot. The 2000 victory of George W. Bush over Al Gore was the result of (Democrat) vote splitting by spoiler candidate Ralph Nader.

Vote splitting can be effectively prevented by changing the voting method. There are multiple approaches to this end, each with its own pros and cons. Many of them rely on the use of ranked ballots. In this kind of ballot, a voter does not have to mark their one preferred candidate, but instead can define a ranking of several candidates from most to least preferred. Once voting is conducted in this way, there are different computational approaches to determine which candidate wins. For an in-depth discussion of vote splitting and the different methods to address it, you can review the book "Gaming the vote: why elections aren't fair (and what we can do about it)" by William Poundstone.

![Questionnare in csv](/assets/img/Questionnare.png)

## Objective 
1. Read the survey data file provided (Superheroes.csv found in the files section of our course page) and store the information in a Python data structure
2. Ask the user which of the four methods described below they want to use to select a winner (the user input can be a number, a letter, a word, etc.)
3. Run an implementation of the chosen voting system and select a winner or declare a draw
4. Inform the user of the results, including total votes and winner

The CSV file used is a questionnaire collected. The voting methods for this project are:

### 1. Plurality voting
Under this method, the candidate who secures the highest number of votes emerges as the winner. To apply this method to our dataset, we simply need to tally the top-ranked superhero for each survey entry (the one ranked at position 1) and then sum up these counts across all survey entries. The superhero with the most top ranks will be declared the winner.

![Winner for Plurality](assets/img/1winner.png)

### 2. Borda voting
This technique, formulated by 18th-century mathematician Jean-Charles de Borda, remains in use today to determine the MLB Most Valuable Player. In this approach, voters assign numerical rankings to each candidate, and the winner is determined by summing up the points allocated to each candidate based on their ranking. To apply this method to our dataset, we need to assign points to each candidate in inverse proportion to their ranking, relative to the total number of options. This implies that a ranking of 1 corresponds to 12 points, while a ranking of 2 corresponds to 11 points, and so on. Candidates without a ranking receive zero points. The superhero with the highest total points is declared the winner.

![Winner for Borda Voting](assets/img/2winner.png)

### 3. Condorcet voting
The Marquis of Condorcet, Marie Jean Antoine Nicolas de Caritat, developed this approach in the 18th century. Condorcet, a French philosopher and mathematician, was a rival of Borda. Nowadays, the Wikimedia foundation and the Linux community utilize Condorcet voting for most internal elections. In Condorcet voting, the winner is determined by identifying the candidate who would defeat every other candidate in a hypothetical head-to-head match.

To apply this method to our data, we need to use the rankings provided in the survey to determine the winner by comparing every possible pair of superheroes. For instance, when comparing Batman and Superman, we tally the number of people who ranked Batman higher (with a lower number) than Superman and the number who ranked Superman higher than Batman. If Batman is preferred by more people, then he emerges as the winner in that pairing. This procedure is repeated for all possible pairings. If one superhero triumphs over every other one in these pairings, they become the Condorcet winner. In cases where no clear winner emerges, the Condorcet method results in a draw.

![Winner for Condorcet Voting](assets/img/3winner.png)

### 4. Approval voting

This approach was formulated by Robert J. Weber, a mathematician at Cornell University, during the 1970s. Although relatively uncommon outside of professional organizations, the United Nations utilizes it to elect its Secretary-General. In approval voting, voters express their support for multiple candidates by providing binary votes (approve or disapprove). The winner is the candidate who receives the most positive votes.

To apply this method to our data, we must calculate the average ranking for each survey entry. Any ranking below the average (with 1 being the best) would be considered an approval, while anything above would be a disapproval. For instance, if a survey entry ranks four superheroes (with rankings 1-4 and an average of 2.5), rankings 1 and 2 would be approvals, and rankings 3 and 4 would be disapprovals. If an entry ranks five superheroes (with rankings 1-5 and an average of 3), rankings 1 and 2 would be approvals, while rankings 4 and 5 would be disapprovals, and ranking 3 would not be considered. By performing this operation for every survey entry, we count the total number of approvals, and the candidate with the highest count emerges as the winner.

![Winner for Approval Voting](assets/img/4winner.png)

## Conclusion 
This project highlights the significance of exploring various voting methods and their computational aspects. The project's importance lies in the fact that different voting methods can lead to different winners in an election. By examining and implementing alternative voting systems, we gain valuable insights into the potential impact on election outcomes and the fairness of the democratic process.

The prevalent one person, one vote principle, represented by plurality voting, is commonly used in elections. However, as demonstrated in the project, this method can give rise to vote splitting, which distorts the true preferences of the electorate and may result in an undesired winner. Understanding this phenomenon is crucial as it sheds light on the limitations of conventional voting systems and underscores the need for exploring alternative approaches.

Ranked ballots, as studied in the project, offer a promising solution to mitigate vote splitting. Allowing voters to express preferences through rankings provides a more nuanced representation of their choices, which can lead to more accurate election results. The computational analysis of these ranked voting systems offers data-driven insights into their implications and potential benefits for achieving more equitable outcomes.

By employing real-world data in the form of a questionnaire-based CSV file, this project enhances its relevance to practical applications in election scenarios. The findings and comparisons of different voting methods emphasize the impact of computational techniques on decision-making processes in democratic societies. This project showcases the ability to use data-driven approaches to address real-world challenges in the realm of election fairness and encourages further investigation into novel voting systems that may lead to more representative and equitable democratic outcomes.
