---
title: "Summary of IC Chemistry Publications"
author: "hjuinj"
date: "2016-08-11"
output: html_document
---


Load packages and establish connection to Mongodb (here my db is located on the default port on my localhost).

{% highlight r %}
library(rmongodb)
library(stringr)
library(ggplot2)
library(knitr)
library(gridExtra)
library(reshape)

mongo <- mongo.create()
if(mongo.is.connected(mongo) == TRUE) {
    db <- mongo.get.databases(mongo)
    coll <- mongo.get.database.collections(mongo, db)
}
{% endhighlight %}

#Staffs
The records are obtained from 120 staffs. We can look at the relative proportion of Doctors and Professors in the department.


{% highlight r %}
df <- data.frame(names = mongo.distinct(mongo, coll, 'from'))
df$isProf <- str_detect(toupper(df$names), "PROFESSOR")
ggplot(df, aes(x = factor(1), fill = isProf) ) + geom_bar()  + coord_polar(theta = "y")+ theme(axis.title.x=element_blank(),        
        axis.text.x=element_blank(),
        axis.title.y=element_blank(),
        axis.text.y=element_blank())
{% endhighlight %}

![plot of chunk unnamed-chunk-2](/Figs/unnamed-chunk-2-1.svg) 

#Publication
There are in total 9417 entries. The entries are of the following types:

{% highlight text %}
## [1] "JOURNAL ARTICLE"  "CONFERENCE PAPER" "BOOK CHAPTER"    
## [4] "PATENT"           "REPORT"           "SOFTWARE"        
## [7] "OTHER"            "BOOK"             "POSTER"
{% endhighlight %}

We can take a look at how many entries of each publication type are there, note the y-axis is on a **log** scale:

{% highlight r %}
df <- mongo.find.all(mongo, coll, fields = list('publication-type' = 1, '_id' = 0), data.frame = T)
ggplot(df, aes(x = publication.type) ) + geom_bar() +  geom_text(aes(label = ..count..), stat = "count", vjust = -1)+ theme(axis.text.x = element_text(angle = 90, hjust = 1)) + scale_y_log10(breaks = c(1,10,100,1000,10000)) 
{% endhighlight %}

![plot of chunk unnamed-chunk-4](/Figs/unnamed-chunk-4-1.svg) 

It is most interesting to look at only journal & conference publications, which are the vast majority of entries anyways. There are 8953 such entries. Bear in mind there are duplicate entries, where IC chemistry staffs collaborated to produce a piece of work.



{% highlight r %}
main <- mongo.find.all(mongo, coll, query=list("$or" = list(list("publication-type" = "JOURNAL ARTICLE"), list("publication-type" = "CONFERENCE PAPER"))), fields = list('publication-type' = 1, 'title' = 1, 'num_citations' = 1, 'journal' = 1, 'year' = 1, 'from' = 1, '_id' = 0))


# Only keeps data entries that have all the header fields defined. 
list2df <- function(list, headers){
    output = list()
    for(i in 1:length(list)){
        record = T
        for(j in headers){
            if(is.null(list[[i]][[j]])){
                record = F
                break
            }
        }
        if(record == T){
            for(j in headers)
                output[[j]] <-  c(output[[j]], list[[i]][[j]])
        }
    }
    return(as.data.frame(output))
}
{% endhighlight %}




{% highlight r %}
# df <- data.frame(journals = unlist(lapply(main, function(i) i$journal)), stringsAsFactors = F)
df <- list2df(main, c('journal', 'title'))
{% endhighlight %}
The 8116 journal submissions are delivered to  1102 different journals. A coarse look at the number of submissions to each of the journals. Have a guess what is the most popular journal(the tallest bar). Bear in mind multiple academics could be have drafted the same paper, this needs to be accounted for.

{% highlight r %}
df <- df[!duplicated(df$title), ]
ggplot(df, aes(x = journal) ) + geom_bar() + theme(axis.text.x=element_blank(),axis.ticks=element_blank())
{% endhighlight %}

![plot of chunk unnamed-chunk-7](/Figs/unnamed-chunk-7-1.svg) 

{% highlight r %}
q <- aggregate(df$journal, by=list(df$journal), length)
colnames(q) <- c("Journal.Names", "Submission")
q <- q[order(q$Submission, decreasing = T),]
kable(tail(q, 10), row.names = F)
{% endhighlight %}



|Journal.Names                                                   | Submission|
|:---------------------------------------------------------------|----------:|
|VIBRATIONAL SPECTROSCOPY                                        |          1|
|WATER ENVIRONMENT RESEARCH                                      |          1|
|WATER SCIENCE AND TECHNOLOGY                                    |          1|
|WEAR                                                            |          1|
|WILEY INTERDISCIPLINARY REVIEWS-COMPUTATIONAL MOLECULAR SCIENCE |          1|
|WILEY INTERDISCIPLINARY REVIEWS-ENERGY AND ENVIRONMENT          |          1|
|ZEITSCHRIFT FUR ANORGANISCHE UND ALLGEMEINE CHEMIE              |          1|
|ZEITSCHRIFT FUR PHYSIK B-CONDENSED MATTER                       |          1|
|Zeitschrift für Physikalische Chemie                           |          1|
|ZHURNAL EKSPERIMENTALNOI I TEORETICHESKOI FIZIKI                |          1|



{% highlight r %}
kable(head(q, 10), row.names = F)
{% endhighlight %}



|Journal.Names                                           | Submission|
|:-------------------------------------------------------|----------:|
|CHEMICAL COMMUNICATIONS                                 |        249|
|JOURNAL OF THE AMERICAN CHEMICAL SOCIETY                |        231|
|JOURNAL OF THE CHEMICAL SOCIETY-CHEMICAL COMMUNICATIONS |        167|
|JOURNAL OF ORGANIC CHEMISTRY                            |        165|
|ABSTRACTS OF PAPERS OF THE AMERICAN CHEMICAL SOCIETY    |        135|
|TETRAHEDRON LETTERS                                     |        135|
|JOURNAL OF CHEMICAL PHYSICS                             |        123|
|PHYSICAL CHEMISTRY CHEMICAL PHYSICS                     |        117|
|JOURNAL OF THE CHEMICAL SOCIETY-PERKIN TRANSACTIONS 1   |        112|
|JOURNAL OF THE CHEMICAL SOCIETY-DALTON TRANSACTIONS     |        106|

Let's look at the top 20 most popular journals:

{% highlight r %}
q$Journal.Names <- factor(q$Journal.Names, levels = q$Journal.Names)
ggplot(q[1:20, ], aes(x = Journal.Names, y = Submission)) + geom_bar(stat = "identity") + theme(axis.text.x = element_text(angle = 90, hjust = 1))
{% endhighlight %}

![plot of chunk unnamed-chunk-8](/Figs/unnamed-chunk-8-1.svg) 
There does not seem to be a significant bias towards any of the three areas of chemistry. 

#Citations

{% highlight r %}
df <- list2df(main, c('title', 'num_citations'))
df$title <- str_trim(df$title)
df <- df[!duplicated(df$title), ]
df <- df[order(df$num_citations, decreasing = T), ]
ggplot(df, aes(x = num_citations)) + geom_bar() + xlim(0, 250) + ylim(0,300)
{% endhighlight %}

![plot of chunk unnamed-chunk-9](/Figs/unnamed-chunk-9-1.svg) 
There are some 'citation beasts' - outliers not included in the above bar chart:

|title                                                                                                                                           | num_citations|
|:-----------------------------------------------------------------------------------------------------------------------------------------------|-------------:|
|A 2ND GENERATION FORCE-FIELD FOR THE SIMULATION OF PROTEINS,NUCLEIC-ACIDS,AND ORGANIC-MOLECULES                                                 |          7810|
|The path forward for biofuels and biomaterials                                                                                                  |          2373|
|A strong regioregularity effect in self-organizing conjugated polymer films and high-efficiency polythiophene: fullerene solar cells            |          1647|
|The search for new-generation olefin polymerization catalysts: Life beyond metallocenes                                                         |          1608|
|N-Heterocyclic Carbenes in Late Transition Metal Catalysis                                                                                      |          1438|
|Liquid-crystalline semiconducting polymers with high charge-carrier mobility                                                                    |          1271|
|TETRAPROPYLAMMONIUM PERRUTHENATE,PR4N+RUO4-,TPAP - A CATALYTIC OXIDANT FOR ORGANIC-SYNTHESIS                                                    |          1243|
|FERROCENE-MEDIATED ENZYME ELECTRODE FOR AMPEROMETRIC DETERMINATION OF GLUCOSE                                                                   |          1224|
|ORGANOMETALLIC COMPOUNDS FOR NONLINEAR OPTICS - THE SEARCH FOR EN-LIGHT-ENMENT                                                                  |          1221|
|Synthesis and function of 3-phosphorylated inositol lipids                                                                                      |          1101|
|N-heterocyclic carbenes as organocatalysts                                                                                                      |           966|
|Development of a dispersion process for carbon nanotubes in an epoxy matrix and the resulting electrical properties                             |           944|
|Ultra-low electrical percolation threshold in carbon-nanotube-epoxy composites                                                                  |           904|
|Charge Photogeneration in Organic Solar Cells                                                                                                   |           879|
|An improved experimental determination of external photoluminescence quantum efficiency                                                         |           856|
|Fabrication and characterization of carbon nanotube/poly(vinyl alcohol) composites                                                              |           856|
|STRUCTURE OF THE INVERTED HEXAGONAL (HII) PHASE,AND NON-LAMELLAR PHASE-TRANSITIONS OF LIPIDS                                                    |           837|
|PHASE-EQUILIBRIA BY SIMULATION IN THE GIBBS ENSEMBLE - ALTERNATIVE DERIVATION,GENERALIZATION AND APPLICATION TO MIXTURE AND MEMBRANE EQUILIBRIA |           825|
|Materials and Applications for Large Area Electronics: Solution-Based Approaches                                                                |           814|
|Novel olefin polymerization catalysts based on iron and cobalt                                                                                  |           809|

#Prof vs Doc
I would expect there is some correlation between the year of publication and the number of citations (the highest cited force-field paper removed):

{% highlight r %}
df <- list2df(main, c('title', 'year', 'num_citations', 'from'))
# df$title <- str_trim(df$title)
# df <- df[!duplicated(df$title), ]
ggplot(df, aes(year, num_citations)) + geom_point() + theme(axis.text.x = element_text(angle = 90, hjust = 1)) + ylim(0, 2500)
{% endhighlight %}

![plot of chunk unnamed-chunk-11](/Figs/unnamed-chunk-11-1.svg) 
Nope, doesn't seem like it. But maybe professors have in a general a higher citation rate than docs?

{% highlight r %}
df$isProf <- str_detect(toupper(df$from), "PROFESSOR")
# ggplot(df, aes(year, num_citations)) + geom_point(aes(color = isProf)) + theme(axis.text.x = element_text(angle = 90, hjust = 1)) + ylim(0, 2500)
ggplot(data = df, mapping = aes(x = num_citations)) + facet_grid(isProf~., scale = 'free') + geom_histogram(data = subset(df, isProf == F), binwidth = 1, fill = "red", alpha = 0.5) + geom_histogram(data = subset(df, isProf == T), binwidth = 1 , fill = "blue", alpha = 0.5) + xlim(0, 250) + ylim(0, 300) 
{% endhighlight %}

![plot of chunk unnamed-chunk-12](/Figs/unnamed-chunk-12-1.svg) 
A clear indication of difference would be a shift of the bottom (professor num_citations) distribution to the right w.r.t the top distribution, which is not seen. However, there is a more visible tail for the bottom distribution than the top. This indicates professors tend to have more higher cited papers.
In addition, the bottom distribution is taller than the top one, mind you this is despite the fact that only about one third of the department are professors. This means an indicator of professors is that they tend to have published more than doctors. A clearer way to demonstrate this is to compare the disbutions of the number of publications for professors and doctors. 


{% highlight r %}
q <- aggregate(df$from, by = list(df$from), length)
colnames(q) <- c('name', 'num_publications')
q$isProf <- str_detect(toupper(q$name), "PROFESSOR")
ggplot(data = q, mapping = aes(x = num_publications)) + facet_grid(isProf~., scale = 'free') + geom_histogram(data = subset(q, isProf == F), fill = "red", alpha = 0.5) + geom_histogram(data = subset(q, isProf == T), fill = "blue", alpha = 0.5) + ylab("Number of Profs / Docs")
{% endhighlight %}

![plot of chunk unnamed-chunk-13](/Figs/unnamed-chunk-13-1.svg) 

#Internal Collaborations
Is there a lot of internal collaborations between staffs? Who collaborates with whom within IC chem? One way to look at that is to tally which staffs have the same publications.

{% highlight r %}
df <- list2df(main, c('from', 'title'))
df$title <- iconv(df$title,"WINDOWS-1252","UTF-8")
df$title <- toupper(df$title)
#df <- df[duplicated(df$title), ]
#q <- aggregate(df$title, list(df$title), length)
#q <- q$Group.1[q$x > 1]
q <- unique(df$title)
# avoid same title by the same author
q <-sapply(q, function(i){
    length(unique(df$from[df$title == i])) 
})
p <- names(q[q > 1])
s <- unique(df$from[df$title %in% p])
{% endhighlight %}
Actually, 1162 pieces of work were collarborative efforts. That is quite a large proportion. 100 staffs were involved in internal collaborations, almost the whole department.

A heatmap can show which staffs work together. Each row and column with a index represents a staff, where the staffs are sorted alphabetically by name. The table below the heatmap shows the index and name mapping. In the heatmap, the lighter the colour, the more collaboration between a pair of staffs, also the higher the number in the cell.

{% highlight r %}
heatmap <- function(matrix, xlabel = NULL, ylabel = NULL, fill = NULL, color= NULL, text_size = 7){
    matrix <- as.data.frame(matrix)
    colors <- c("steelblue", "seagreen", "darkorchid", "maroon")
    melt <- melt(matrix)
    if(ncol(melt) == 2){
        melt$variable1 <- melt$variable
        melt$variable2 <- rep(rownames(matrix), nrow(matrix))
        melt$variable1 <- factor(melt$variable1, levels = (unique(as.character(rownames(matrix)))))
        melt$variable2 <- factor(melt$variable2, levels = rev(unique(as.character(rownames(matrix)))))
    }
    p <- ggplot(melt,aes(x = variable1, y = variable2)) + geom_tile(aes(fill = value), colour = "white") + scale_fill_gradient(high = "white", low = "black")
    p <- p + geom_text(aes(fill = value, label = round(value,2)), size = text_size) + labs(x = xlabel, y = ylabel, fill = fill) + theme(axis.text.x = element_text(angle = 90)) + theme(legend.position = "none")
}

staffs <- as.character(sort(s))
matrix <- matrix(0, nrow = length(staffs), ncol = length(staffs))
colnames(matrix) <- rownames(matrix) <- staffs
collaborations <- lapply(p,function(i) df$from[(df$title == i)] )
for(i in collaborations){
    for(j in 1:(length(i) - 1)){
        for(k in (j + 1):length(i)){
#             print(str_c(i[k],i[j]))
#             print(i[k] %in% colnames(matrix))
#             print(i[k] %in% rownames(matrix))
#             print(i[j] %in% rownames(matrix))
#             print(i[j] %in% colnames(matrix))
            r <- which(i[j] == staffs)
            c <- which(i[k] == staffs)
            matrix[r, c] <- matrix[c, r] <- 1 + matrix[r, c]
        }
    }
}    
colnames(matrix) <- rownames(matrix) <- 1:length(staffs)
p <- heatmap(matrix, text_size = 3)
p
{% endhighlight %}

![plot of chunk unnamed-chunk-15](/Figs/unnamed-chunk-15-1.svg) 

{% highlight r %}
kable(data.frame(Index = (1:length(staffs)), Name = staffs), row.names = F)
{% endhighlight %}



| Index|Name                                               |
|-----:|:--------------------------------------------------|
|     1|Dr Abby Casey                                      |
|     2|Dr Adam R J Clancy                                 |
|     3|Dr Agostino Cilibrizzi                             |
|     4|Dr Aleksandar Ivanov                               |
|     5|Dr Alexander J W Thom                              |
|     6|Dr Alexandra Simperler FHEA                        |
|     7|Dr Andrew E Ashley                                 |
|     8|Dr Artem Bakulin                                   |
|     9|Dr Balaji Purushothaman                            |
|    10|Dr Barbara Montanari                               |
|    11|Dr Beinn Muir                                      |
|    12|Dr Charles R E Romain                              |
|    13|Dr Colin R Crick                                   |
|    14|Dr David A Widdowson                               |
|    15|Dr Duncan R Casey                                  |
|    16|Dr Elena M Barreiro                                |
|    17|Dr Garry Rumbles                                   |
|    18|Dr George J P Britovsek                            |
|    19|Dr Giuseppe Mallia                                 |
|    20|Dr Guido Bolognesi                                 |
|    21|Dr Hannah S Leese                                  |
|    22|Dr Ian R Gould                                     |
|    23|Dr James A Bull                                    |
|    24|Dr James D Wilton-Ely                              |
|    25|Dr James H Bannock                                 |
|    26|Dr Jennifer A Garden                               |
|    27|Dr Joao Pedro B C Malhado                          |
|    28|Dr Jordi Bures Amat                                |
|    29|Dr Joshua B Edel                                   |
|    30|Dr Laura M C Barter                                |
|    31|Dr Leonora Velleman                                |
|    32|Dr Luke X Reynolds                                 |
|    33|Dr Marina K Kuimova                                |
|    34|Dr Mark R Crimmin                                  |
|    35|Dr Markus Ritzefeld                                |
|    36|Dr Matthew J Fuchter                               |
|    37|Dr Mimi Hii                                        |
|    38|Dr Mustafa K Bayazit                               |
|    39|Dr Nicholas J Brooks                               |
|    40|Dr Olga Kuzmina                                    |
|    41|Dr Oscar Ces                                       |
|    42|Dr Patricia A Hunt                                 |
|    43|Dr Paul Wilde                                      |
|    44|Dr Philip Miller                                   |
|    45|Dr Pierre Boufflet                                 |
|    46|Dr Remigiusz A Serwa                               |
|    47|Dr Rob Davies                                      |
|    48|Dr Robert Menzel                                   |
|    49|Dr Robert V Law                                    |
|    50|Dr Rudiger Woscholski                              |
|    51|Dr Saif A Haque                                    |
|    52|Dr Sanjiv Sharma                                   |
|    53|Dr Silvia Diez-Gonzalez                            |
|    54|Dr Stoichko Dimitrov                               |
|    55|Dr Thomas Lanyon-Hogg                              |
|    56|Dr Thomas Rath                                     |
|    57|Dr Tim Albrecht                                    |
|    58|Dr Xiaoe Li                                        |
|    59|Dr Yuval Elani                                     |
|    60|Dr Zhuping Fei                                     |
|    61|Emeritus Professor Andrew B Holmes AM FRS FAA FTSE |
|    62|Emeritus Professor David Phillips                  |
|    63|Emeritus Professor Henry S Rzepa                   |
|    64|Emeritus Professor Michael Spiro                   |
|    65|Emeritus Professor William P Griffith              |
|    66|Mr Yoni Weiner                                     |
|    67|Ms Elisa Collado Fregoso                           |
|    68|Professor Alan Armstrong                           |
|    69|Professor Alan Spivey                              |
|    70|Professor Alexei A Kornyshev                       |
|    71|Professor Anthony G M Barrett FRS, FMedSci         |
|    72|Professor Anthony R J Kucernak                     |
|    73|Professor Charlotte K Williams                     |
|    74|Professor Chris Braddock                           |
|    75|Professor David M L Goodgame                       |
|    76|Professor David R Klug                             |
|    77|Professor David Scheschkewitz                      |
|    78|Professor Ed Tate BSc PhD FRSC FRSB                |
|    79|Professor Fernando Bresme                          |
|    80|Professor Iain McCulloch                           |
|    81|Professor James R Durrant                          |
|    82|Professor John C de Mello                          |
|    83|Professor John M Seddon                            |
|    84|Professor Keith Willison                           |
|    85|Professor Martin J Heeney                          |
|    86|Professor Michael J Bearpark                       |
|    87|Professor Mike Robb FRS                            |
|    88|Professor Milo S P Shaffer                         |
|    89|Professor Nicholas J Long                          |
|    90|Professor Nicholas M Harrison                      |
|    91|Professor Nick Quirke                              |
|    92|Professor Paul D Lickiss                           |
|    93|Professor Philip J Parsons                         |
|    94|Professor Ramon Vilar Compte                       |
|    95|Professor Richard Templer                          |
|    96|Professor Robin J Leatherbarrow                    |
|    97|Professor Sophia Yaliraki                          |
|    98|Professor Sue Gibson                               |
|    99|Professor Tony Cass                                |
|   100|Professor Tony Gee                                 |

One can see Prof Heaney and Prof McCulloch has collaborated the most. Most of the collaborations were duos. In the most extreme case, 6 staffs collaborated on 5 different piece of work:

{% highlight r %}
ggplot(data.frame(x = sapply(collaborations, function(i) length(i))), aes(x) ) + geom_bar() +  geom_text(aes(y = ..count.. , label = ..count..), stat = "count", vjust = -1) + scale_y_log10() + scale_x_discrete() + xlab("Number of staffs contributed to the paper")
{% endhighlight %}

![plot of chunk unnamed-chunk-16](/Figs/unnamed-chunk-16-1.svg) 


There is a lot a lot a lot more that can be done with the data, employing more sophisticated analysis, which I might venture into if one day I feel like it. 
The natural language processing done here is very crude and hence the numbers here are by no means absoluatly accurate. But I believe the general inferences are sound.
