#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# PROGRAMMER: Kidus Worku
# DATE CREATED: August 22, 2022                                  
# REVISED DATE: August 24, 2022
# PURPOSE: Prins a tabular form of all the CNN models for summarizing and presenting the final putcomes

# Imports python modules
from time import time

# Imports functions created for this program
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats 

# Main program function defined below
def main(): 
    vgg_data = ['VGG'] 
    resnet_data = ['ResNet'] 
    alexnet_data = ['AlexNet']  
    
    n_vgg_data = ['VGG'] 
    n_resnet_data = ['ResNet'] 
    n_alexnet_data = ['AlexNet'] 
    
    # **** Measure for VGG ****
    # Measures total program runtime by collecting start time
    start_time_vgg = time()
    results_vgg = get_pet_labels("pet_images/")
    classify_images("pet_images/", results_vgg, "vgg")
    adjust_results4_isadog(results_vgg, "dognames.txt")
    results_stats_vgg = calculates_results_stats(results_vgg)
    end_time_vgg = time()
    
    tot_time_vgg = end_time_vgg - start_time_vgg
    tot_time_formatted_vgg = str(int((tot_time_vgg/3600)))+":"+str(int((tot_time_vgg%3600)/60))+":"+str(int((tot_time_vgg%3600)%60)) 
    
    # **** Measure for ResNet ****
    # Measures total program runtime by collecting start time
    start_time_resnet = time()
    results_resnet = get_pet_labels("pet_images/")
    classify_images("pet_images/", results_resnet, "resnet")
    adjust_results4_isadog(results_resnet, "dognames.txt")
    results_stats_resnet = calculates_results_stats(results_resnet)
    end_time_resnet = time()
    
    tot_time_resnet = end_time_resnet - start_time_resnet
    tot_time_formatted_resnet = str(int((tot_time_resnet/3600)))+":"+str(int((tot_time_resnet%3600)/60))+":"+str(int((tot_time_resnet%3600)%60))
    
    # **** Measure for AlexNet ****
    # Measures total program runtime by collecting start time
    start_time_alexnet = time()
    results_alexnet = get_pet_labels("pet_images/") 
    classify_images("pet_images/", results_alexnet, "alexnet")
    adjust_results4_isadog(results_alexnet, "dognames.txt") 
    results_stats_alexnet = calculates_results_stats(results_alexnet)
    end_time_alexnet = time()
    
    tot_time_alexnet = end_time_alexnet - start_time_alexnet 
    tot_time_formatted_alexnet = str(int((tot_time_alexnet/3600)))+":"+str(int((tot_time_alexnet%3600)/60))+":"+str(int((tot_time_alexnet%3600)%60))
    
    # *** Printing total numbers
    n_resnet_data.extend([results_stats_resnet['n_images'],
                       results_stats_resnet['n_dogs_img'],
                       results_stats_resnet['n_notdogs_img']])
    
    n_alexnet_data.extend([results_stats_alexnet['n_images'],
                        results_stats_alexnet['n_dogs_img'],
                        results_stats_alexnet['n_notdogs_img']])
    
    n_vgg_data.extend([results_stats_vgg['n_images'],
                    results_stats_vgg['n_dogs_img'],
                    results_stats_vgg['n_notdogs_img']]) 
    
    n_cnn_data = []
    n_cnn_data.extend([n_resnet_data,
                    n_alexnet_data,
                    n_vgg_data])

    print("\nResults: Number of Images\n")
    print("{:<8} {:<17} {:<17} {:<17}".format('CNN Model', '# Total Images', '# Dog Images', '# Not-a-Dog Images')) 
    
    for data in n_cnn_data:
        print("{:<8} {:<17} {:<17} {:<17}".format(data[0], data[1], data[2], data[3]))     
    
    
    # Print Percentage Statistics
    resnet_data.extend([results_stats_resnet['pct_correct_notdogs'],
                       results_stats_resnet['pct_correct_dogs'],
                       results_stats_resnet['pct_correct_breed'],
                       results_stats_resnet['pct_match'],
                       tot_time_formatted_resnet])
    
    alexnet_data.extend([results_stats_alexnet['pct_correct_notdogs'],
                        results_stats_alexnet['pct_correct_dogs'],
                        results_stats_alexnet['pct_correct_breed'],
                        results_stats_alexnet['pct_match'],
                        tot_time_formatted_alexnet])
    
    vgg_data.extend([results_stats_vgg['pct_correct_notdogs'],
                    results_stats_vgg['pct_correct_dogs'],
                    results_stats_vgg['pct_correct_breed'],
                    results_stats_vgg['pct_match'],
                    tot_time_formatted_vgg]) 
    
    cnn_data = []
    cnn_data.extend([resnet_data,
                    alexnet_data,
                    vgg_data])

    
    print("\nResults: Performance\n")
    print("{:<8} {:<17} {:<17} {:<17} {:<17} {:<17}".format('CNN Model', '% Not-a-Dog Correct', '% is-a-Dog Correct', '% Breeds Correct', '% Match Labels', 'Time Elapsed')) 
    
    for data in cnn_data:
        print("{:<8} {:<17.2f} {:<17.2f} {:<17.2f} {:<17.2f} {:<6}".format(data[0], data[1], data[2], data[3], data[4], data[5])) 
        
# Call to main function to run the program
if __name__ == "__main__":
    main()
    