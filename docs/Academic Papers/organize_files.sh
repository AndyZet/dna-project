#!/bin/bash
# Script to organize Academic Papers directory

cd "/Users/andrzejzak/DNA Project/docs/Academic Papers"

# Remove remaining duplicates
rm -f "K. Zhur - The Rurikids The First Experience of Reconstructing the Genetic Portrait of the Ruling Family of Medieval Rus' Based on  (1).pdf"

# Move remaining genetic studies
[ -f "M. Figlerowicz - Piast State Society – History Deciphered from DNA [2025].pdf" ] && mv "M. Figlerowicz - Piast State Society – History Deciphered from DNA [2025].pdf" "01_Genetic_Studies/2025_Figlerowicz_Piast_State_Society_DNA.pdf"

# Move Rus/Rurikids studies
[ -f "A. Shchavelev - The People Rus' in the Ninth – Middle Eleventh Centuries New Approaches to the Study of Ethnogenesis and Politogen.pdf" ] && mv "A. Shchavelev - The People Rus' in the Ninth – Middle Eleventh Centuries New Approaches to the Study of Ethnogenesis and Politogen.pdf" "02_Medieval_Rus_Rurikids/2023_Shchavelev_People_Rus_Ethnogenesis.pdf"
[ -f "Petr S. Stefanovich - The Political Organization of Rus' in the 10th Century [2016].pdf" ] && mv "Petr S. Stefanovich - The Political Organization of Rus' in the 10th Century [2016].pdf" "02_Medieval_Rus_Rurikids/2016_Stefanovich_Political_Organization_Rus.pdf"
[ -f "Stefanovich_2016_The_Political_Organization_of_Rus_in_the_10th_Century.pdf" ] && mv "Stefanovich_2016_The_Political_Organization_of_Rus_in_the_10th_Century.pdf" "02_Medieval_Rus_Rurikids/2016_Stefanovich_Political_Organization_Rus_alt.pdf"
[ -f "Márta Font - Практика имянаречений у князей Древней Руси – как исторический источник [2022].pdf" ] && mv "Márta Font - Практика имянаречений у князей Древней Руси – как исторический источник [2022].pdf" "02_Medieval_Rus_Rurikids/2022_Font_Naming_practices_Rus_princes.pdf"
[ -f "Петро Дешко - The Celtic Theory of the Origins of Rus' as an Alternative to Normanism and the Concept of the «Old Rus' Ethnicity» .pdf" ] && mv "Петро Дешко - The Celtic Theory of the Origins of Rus' as an Alternative to Normanism and the Concept of the «Old Rus' Ethnicity» .pdf" "02_Medieval_Rus_Rurikids/2023_Deshko_Celtic_Theory_Rus_Origins.pdf"
[ -f "mikheev2009b_book.pdf" ] && mv "mikheev2009b_book.pdf" "02_Medieval_Rus_Rurikids/2009_Mikheev_Rurikids_monograph.pdf"

# Move Bodzia/Cieple files
[ -f "Buko_etal_2013_Bodzia_AKB_43_3.pdf" ] && mv "Buko_etal_2013_Bodzia_AKB_43_3.pdf" "03_Bodzia_Cieple_Archaeology/2013_Buko_etal_Bodzia_cemetery.pdf"
[ -f "Cieple_-_elitarna_nekropola.pdf" ] && mv "Cieple_-_elitarna_nekropola.pdf" "03_Bodzia_Cieple_Archaeology/Cieple_elitarna_nekropola.pdf"
[ -f "Cieple_-_elitarna_nekropola.md" ] && mv "Cieple_-_elitarna_nekropola.md" "03_Bodzia_Cieple_Archaeology/Cieple_elitarna_nekropola.md"

# Move reference materials
[ -f "Beznosyuk_2019_The_Rurikids.html" ] && mv "Beznosyuk_2019_The_Rurikids.html" "05_Reference_Materials/Beznosyuk_2019_Rurikids.html"
[ -f "FMG_MedLands_Swabia_Konradiner.html" ] && mv "FMG_MedLands_Swabia_Konradiner.html" "05_Reference_Materials/FMG_MedLands_Swabia_Konradiner.html"
[ -f "Vanbrabant_2015_From_the_rus_on_the_littus_Ruthenicum_to_the_Russian_people.html" ] && mv "Vanbrabant_2015_From_the_rus_on_the_littus_Ruthenicum_to_the_Russian_people.html" "05_Reference_Materials/Vanbrabant_2015_Rus_Ruthenicum.html"
[ -f "Elicit - extract-results-review-8aefa20a-f5fd-4895-9251-47b725cf0810.csv" ] && mv "Elicit - extract-results-review-8aefa20a-f5fd-4895-9251-47b725cf0810.csv" "05_Reference_Materials/Elicit_extract_results.csv"
[ -f "README_download_status.md" ] && mv "README_download_status.md" "05_Reference_Materials/README_download_status.md"

# Handle unidentified file
[ -f "703405v1.full.pdf" ] && mv "703405v1.full.pdf" "05_Reference_Materials/703405v1_unidentified.pdf"

echo "Organization complete!"
