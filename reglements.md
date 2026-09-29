---
layout: default
title: "Règlements généraux proposés"
subtitle: "Cadre de gouvernance démocratique, éthique et sociocratique de COHABITAT.CC"
description: "Projet de règlements généraux de COHABITAT.CC (personne morale sans but lucratif sous la Partie III). Document ouvert aux propositions d'amendements par demande de fusion (pull request)."
permalink: /reglements/
image: "/assets/images/cohabitat_concept_banner.jpg"
---

<header class="bylaws-hero">
  <div class="site-container text-center">
    <div class="bylaws-badge">Gouvernance ouverte & Démocratie par les pairs</div>
    <h1 class="bylaws-title">Règlements généraux proposés</h1>
    <p class="bylaws-subtitle">
      Projet de charte de fonctionnement et de gouvernance démocratique de <strong>COHABITAT.CC</strong>.
    </p>
    <div class="bylaws-pr-banner">
      <div class="bylaws-pr-icon">🐙</div>
      <div class="bylaws-pr-text">
        <strong>Document vivant &amp; collaboratif :</strong> Chaque article est modulaire. Tout membre ou partie prenante peut proposer une bonification ou un amendement directement par demande de fusion (pull request).
      </div>
      <a href="https://github.com/cohabitat-cc/www.cohabitat.cc/tree/main/_reglements" target="_blank" rel="noopener noreferrer" class="bylaws-pr-btn">
        <svg width="16" height="16" viewBox="0 0 16 16" fill="currentColor" style="vertical-align: -2px; margin-right: 6px;"><path fill-rule="evenodd" d="M7.177 3.073L9.573.677A.25.25 0 0110 .854v4.792a.25.25 0 01-.427.177L7.177 3.427a.25.25 0 010-.354zM3.75 2.5a.75.75 0 100 1.5.75.75 0 000-1.5zm-2.25.75a2.25 2.25 0 113 2.122v5.256a2.251 2.251 0 11-1.5 0V5.372A2.25 2.25 0 011.5 3.25zM11 2.5h-1V4h1a1 1 0 011 1v5.628a2.251 2.251 0 101.5 0V5A2.5 2.5 0 0011 2.5zm1 10.25a.75.75 0 111.5 0 .75.75 0 01-1.5 0zM3.75 12a.75.75 0 100 1.5.75.75 0 000-1.5z"></path></svg>
        Dossier des règlements (GitHub)
      </a>
    </div>
  </div>
</header>

<section class="bylaws-section">
  <div class="site-container bylaws-layout">

    <!-- Table des matières latérale générée dynamiquement -->
    <aside class="bylaws-toc-sidebar">
      <div class="bylaws-toc-sticky">
        <h3 class="bylaws-toc-heading">Sommaire des articles</h3>
        <nav class="bylaws-toc-nav">
          {% assign sorted_articles = site.reglements | sort: 'numero' %}
          {% for art in sorted_articles %}
            <a href="#{{ art.slug }}">{{ art.numero }}. {{ art.titre }}</a>
          {% endfor %}
        </nav>
        <div class="bylaws-toc-meta">
          <span>Statut : <strong>Projet v1.0 (en consultation)</strong></span>
          <span>Cadre : <strong>Loi sur les compagnies (Partie III)</strong></span>
          <span style="margin-top: 0.5rem; display: block;">
            <a href="{{ '/gouvernance/' | relative_url }}" style="color: var(--color-primary); font-weight: 600; text-decoration: underline;">
              Guide des demandes de fusion &rarr;
            </a>
          </span>
        </div>
      </div>
    </aside>

    <!-- Contenu juridique principal -->
    <article class="bylaws-content">

      <!-- AVERTISSEMENT PRÉAMBULE -->
      <div class="bylaws-preamble-box">
        <h4>Préambule et esprit du texte</h4>
        <p>
          Les présents règlements généraux définissent les assises juridiques, éthiques et opérationnelles de <strong>COHABITAT.CC</strong>. Conçus pour allier la rigueur du droit corporatif québécois des personnes morales sans but lucratif aux pratiques modernes d'autogestion sociocratique et de gouvernance ouverte (open source), ils visent à pérenniser des habitats collectifs résilients et déspéculés.
        </p>
        <p>
          Chaque article est un fichier Markdown indépendant dans le dossier <code>_reglements/</code>, permettant à toute personne de proposer des bonifications ponctuelles sans risque de casser la structure du document global.
        </p>
      </div>

      <!-- ARTICLES MODULAIRES ITÉRÉS DÉPUIS LA COLLECTION -->
      {% for art in sorted_articles %}
      <section id="{{ art.slug }}" class="bylaws-article-block">
        <div class="article-header">
          <span class="article-num">Article {{ art.numero }}</span>
          <h2 class="article-title">{{ art.titre }}</h2>
        </div>

        <div class="bylaws-article-body">
          {{ art.content }}
        </div>

        <div class="article-edit-bar">
          <a href="https://github.com/cohabitat-cc/www.cohabitat.cc/edit/main/{{ art.path }}" target="_blank" rel="noopener noreferrer" class="article-edit-btn">
            <svg width="14" height="14" viewBox="0 0 16 16" fill="currentColor"><path d="M11.013 1.427a1.75 1.75 0 012.474 0l1.086 1.086a1.75 1.75 0 010 2.474l-8.61 8.61c-.21.21-.47.364-.756.445l-3.251.93a.75.75 0 01-.927-.928l.929-3.25a1.75 1.75 0 01.445-.758l8.61-8.61zm1.414 1.06a.25.25 0 00-.354 0L10.811 3.75l1.439 1.44 1.263-1.263a.25.25 0 000-.354l-1.086-1.086zM10.05 4.51L3.924 10.635a.25.25 0 00-.064.108l-.558 1.953 1.953-.558a.245.245 0 00.108-.064l6.126-6.127L10.05 4.51z"></path></svg>
            Proposer une modification à l'Article {{ art.numero }} sur GitHub
          </a>
        </div>
      </section>
      {% endfor %}

      <!-- Appel à contribution -->
      <div class="bylaws-action-footer">
        <h3>Participer à la rédaction de nos règlements</h3>
        <p>Une question juridique, une précision sur le fonctionnement des cercles ou une idée d'amélioration pour notre charte ? Proposez une modification en quelques clics sur GitHub.</p>
        <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap; margin-top: 1.5rem;">
          <a href="https://github.com/cohabitat-cc/www.cohabitat.cc/tree/main/_reglements" target="_blank" rel="noopener" class="action-btn">
            Consulter le dossier des règlements sur GitHub
          </a>
          <a href="{{ '/gouvernance/' | relative_url }}" class="btn-secondary" style="padding: 0.85rem 1.8rem; border-radius: 9999px; font-weight: 600; text-decoration: none; display: inline-block;">
            Comprendre le processus de gouvernance par demande de fusion (pull request)
          </a>
        </div>
      </div>

    </article>
  </div>
</section>

<script>
  document.addEventListener('DOMContentLoaded', function() {
    // Transformation progressive du Markdown sémantique (h3 + paragraphes) vers le rendu .clause
    document.querySelectorAll('.bylaws-article-body').forEach(function(body) {
      // Détecte et stylise l'intro de l'article avant le premier h3
      var firstH3 = body.querySelector('h3');
      if (firstH3) {
        var prev = firstH3.previousElementSibling;
        while (prev) {
          if (prev.tagName === 'P') {
            prev.classList.add('article-intro');
          }
          prev = prev.previousElementSibling;
        }
      }

      var h3List = Array.from(body.querySelectorAll('h3'));
      h3List.forEach(function(h3) {
        var text = h3.textContent.trim();
        var match = text.match(/^(\d+\.\d+)\s*(.*)$/);
        if (!match) return;

        var num = match[1];
        var title = match[2];
        var clauseAnchorId = 'art-' + num.replace('.', '-');

        // Conteneur de clause
        var clauseEl = document.createElement('div');
        clauseEl.className = 'clause';
        clauseEl.id = clauseAnchorId;

        // Numéro de clause (ex: 1.1)
        var idEl = document.createElement('span');
        idEl.className = 'clause-id';
        idEl.textContent = num;

        // Corps de la clause
        var bodyEl = document.createElement('div');
        bodyEl.className = 'clause-body';

        // Regroupe tous les éléments frères jusqu'au prochain h3
        var next = h3.nextElementSibling;
        var elementsToMove = [];
        while (next && next.tagName !== 'H3') {
          elementsToMove.push(next);
          next = next.nextElementSibling;
        }

        // Intègre le titre en gras
        if (title && elementsToMove.length > 0 && elementsToMove[0].tagName === 'P') {
          var strongTitle = document.createElement('strong');
          strongTitle.textContent = title + (title.endsWith(':') ? ' ' : ' : ');
          elementsToMove[0].prepend(strongTitle);
        } else if (title) {
          var titleDiv = document.createElement('div');
          titleDiv.style.marginBottom = '0.35rem';
          titleDiv.innerHTML = '<strong>' + title + '</strong>';
          bodyEl.appendChild(titleDiv);
        }

        elementsToMove.forEach(function(el) {
          bodyEl.appendChild(el);
        });

        clauseEl.appendChild(idEl);
        clauseEl.appendChild(bodyEl);

        h3.parentNode.insertBefore(clauseEl, h3);
        h3.remove();
      });
    });

    // Gestion du défilement fluide vers une ancre spécifique (#art-1-1)
    if (window.location.hash) {
      var target = document.querySelector(window.location.hash);
      if (target) {
        setTimeout(function() {
          target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }, 150);
      }
    }
  });
</script>
