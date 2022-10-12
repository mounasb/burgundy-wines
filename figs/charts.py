import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')


# # IMPORTS
# wines = pd.read_csv('data/wines_clean.csv', index_col=[0])
# wines_fr = pd.read_csv('data/wines_fr.csv', index_col=[0])
# wines_pinot = pd.read_csv('data/wines_pinot.csv', index_col=[0])


# 9 PLOTS (NOTES, PRIX, MILLESIMES)
def fig_points(wines, wines_fr, wines_pinot):
    mean_points = f"(moyenne : {round(wines.points.mean(), 1)})"
    mean_fr_points = f"(moyenne : {round(wines_fr.points.mean(), 1)})"
    mean_pinot_points = f"(moyenne : {round(wines_pinot.points.mean(), 1)})"

    fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1, figsize=(8,17))
    # plt.subplots_adjust(hspace = 0.2)
    # plt.subplots_adjust(wspace = 0.3)
    # plt.suptitle('Comparatif des notes : international vs France vs Pinot Noir', y=1.0, size=14, weight='bold')

    sns.countplot(x=wines['points'], color='#4daf4a', ax=ax1).set(xlabel='', ylabel='')
    ax1.set_title(f'Notes - International {mean_points}', y=1.02, size=10, weight='bold')

    sns.countplot(x=wines_fr['points'], color='#377eb8', ax=ax2).set(xlabel='', ylabel='')
    ax2.set_title(f'Notes - France {mean_fr_points}', y=1.02, size=10, weight='bold')

    sns.countplot(x=wines_pinot['points'], color='#c13639', ax=ax3).set(xlabel='', ylabel='')
    ax3.set_title(f'Notes - Pinot Noir {mean_pinot_points}', y=1.02, size=10, weight='bold')

    return fig


def fig_prices(wines, wines_fr, wines_pinot):
    mean_price = f"(moyenne : {round(wines.price.mean(), 1)}$)"
    mean_fr_price = f"(moyenne : {round(wines_fr.price.mean(), 1)}$)"
    mean_pinot_price = f"(moyenne : {round(wines_pinot.price.mean(), 1)}$)"

    fig, (ax4, ax5, ax6) = plt.subplots(nrows=3, ncols=1, figsize=(8,17))

    sns.histplot(x=wines['price'], color='#4daf4a', ax=ax4).set(xlabel='', ylabel='')
    ax4.set_title(f'Prix - International {mean_price}', y=1.02, size=10, weight='bold')

    sns.histplot(x=wines_fr['price'], color='#377eb8', ax=ax5).set(xlabel='', ylabel='')
    ax5.set_title(f'Prix - France {mean_fr_price}', y=1.02, size=10, weight='bold')

    sns.histplot(x=wines_pinot['price'], color='#c13639', ax=ax6).set(xlabel='', ylabel='')
    ax6.set_title(f'Prix - Pinot Noir {mean_pinot_price}', y=1.02, size=10, weight='bold')

    return fig


def fig_millesimes(wines, wines_fr, wines_pinot):

    fig, (ax7, ax8, ax9) = plt.subplots(nrows=3, ncols=1, figsize=(8,17))

    # Millésimes
    sns.histplot(x=wines['millesime'], color='#4daf4a', bins=50, ax=ax7).set(xlabel='', ylabel='')
    ax7.set_title(f'Millésimes - International', y=1.02, size=12, weight='bold')

    sns.histplot(x=wines_fr['millesime'], color='#377eb8', bins=50, ax=ax8).set(xlabel='', ylabel='')
    ax8.set_title(f'Millésimes - France', y=1.02, size=12, weight='bold')

    sns.histplot(x=wines_pinot['millesime'], color='#c13639', bins=50, ax=ax9).set(xlabel='', ylabel='')
    ax9.set_title(f'Millésimes - Pinot Noir', y=1.02, size=12, weight='bold')

    return fig


def fig_countries(wines, wines_pinot):
    fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(13,20))
    plt.subplots_adjust(hspace = 0.3)

    sns.barplot(data=wines, x=wines['country'].value_counts().index[:12], y=wines['country'].value_counts().values[:12],  palette='Set2', ax=ax1)
    ax1.set_title('Nombre de références par pays (tous cépages)', y=1.02, size=14, weight='bold')
    ax1.set(xlabel='', ylabel='Nombre de vins')
    ax1.set_xticklabels(ax1.get_xticklabels(), 
                        rotation=45, 
                        horizontalalignment='right',
                        fontweight='light',
                        fontsize='large')

    sns.barplot(data=wines_pinot, x=wines_pinot['country'].value_counts()[:15].index, y=wines_pinot['country'].value_counts()[:15].values, palette='Set2', ax=ax2)
    ax2.set_title('Nombre de références de Pinot Noir par pays', y=1.02, size=14, weight='bold')
    ax2.set(xlabel='', ylabel='Nombre de vins')
    ax2.set_xticklabels(
    ax2.get_xticklabels(), 
    rotation=45, 
    horizontalalignment='right',
    fontweight='light',
    fontsize='large')

    return fig


def fig_varieties(wines):
    fig, ax = plt.subplots(figsize=(13,7))
    sns.barplot(data=wines, x=wines['variety'].value_counts().index[:15], y=wines['variety'].value_counts().values[:15],  palette='Set2', ax=ax)
    
    plt.title('Nombre de références par cépage (les 15 principaux)', y=1.02, size=14, weight='bold')
    plt.ylabel('Nombre de références')
    plt.xlabel('')
    ax.set_xticklabels(ax.get_xticklabels(), 
                       rotation=45, 
                       horizontalalignment='right',
                       fontweight='light',
                       fontsize='large')

    return fig


def fig_pinot_province(wines_pinot):
    provinces_pinot_fr = wines_pinot[wines_pinot['country'] == 'France']['province'].value_counts()

    fig, ax = plt.subplots(figsize=(13,7))
    plt.title('Régions productrices de Pinot Noir en France', y=1.02, size=14, weight='bold')

    sns.barplot(data=wines_pinot, x=provinces_pinot_fr.index, y=provinces_pinot_fr.values,  color='#c13639', ax=ax)
    ax.set(xlabel='', ylabel='Nombre de vins')
    ax.set_xticklabels(
        ax.get_xticklabels(), 
        rotation=45, 
        horizontalalignment='right',
        fontweight='light',
        fontsize='large')

    return fig


def fig_variety_points(wines):

    fig, ax = plt.subplots(figsize=(13,7))
    plt.title('Notes des cépages', y=1.02, size=14, weight='bold')

    
    sns.barplot(data=wines_pinot, x=provinces_pinot_fr.index, y=provinces_pinot_fr.values,  color='#c13639', ax=ax)
    ax.set(xlabel='', ylabel='Nombre de vins')
    ax.set_xticklabels(
        ax.get_xticklabels(), 
        rotation=45, 
        horizontalalignment='right',
        fontweight='light',
        fontsize='large')

    return fig