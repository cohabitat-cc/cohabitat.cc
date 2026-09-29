---
layout: default
title: "Gouvernance ouverte & Processus décisionnel"
subtitle: "Guide pratique de prise de décision par consentement et de modification collaborative par Pull Request"
description: "Comment participer à la gouvernance de COHABITAT.CC : guide pour proposer des amendements aux règlements et comprendre le fonctionnement des résolutions du Conseil d'administration par Pull Request."
permalink: /gouvernance/
image: "/assets/images/cohabitat_concept_banner.jpg"
---

<header class="about-hero">
  <div class="site-container text-center">
    <div class="about-badge">Démocratie ouverte &amp; Sociocratie</div>
    <h1 class="about-hero-title">Gouvernance ouverte &amp; Décision par les pairs</h1>
    <p class="about-hero-tagline">
      Chez COHABITAT.CC, nos statuts, nos règlements et les décisions de notre Conseil d'administration sont gérés en code ouvert sous contrôle de version, accessibles et modifiables par consentement.
    </p>
  </div>
</header>

<section class="about-section">
  <div class="site-container">

    <!-- Encadré Principes Fondamentaux -->
    <div class="legal-status-card" style="margin-bottom: 4rem;">
      <div class="legal-status-header">
        <span class="legal-status-pill">
          <span class="pulse-dot"></span>
          Cadre statutaire
        </span>
        <h2 class="legal-status-title">Pourquoi une gouvernance par Pull Request ?</h2>
      </div>
      <p class="legal-status-desc">
        La gestion traditionnelle des organismes sans but lucratif repose souvent sur des classeurs de résolutions poussiéreux ou des documents Word aux versions éparpillées. Chez <strong>COHABITAT.CC</strong>, nous appliquons les meilleures pratiques du logiciel libre (<em>Open Source Governance</em>) :
      </p>
      <div class="legal-meta-grid">
        <div class="legal-meta-item">
          <h4>Traçabilité inaltérable</h4>
          <p>Chaque virgule modifiée est horodatée, documentée et attribuée à son auteur.</p>
        </div>
        <div class="legal-meta-item">
          <h4>Transparence radicale</h4>
          <p>Les délibérations et motivations sont publiques et consultables en tout temps.</p>
        </div>
        <div class="legal-meta-item">
          <h4>Sociocratie vécue</h4>
          <p>Décision par consentement : recherche d'objections raisonnables plutôt que vote partisan.</p>
        </div>
        <div class="legal-meta-item">
          <h4>Simplicité modulaire</h4>
          <p>Des fichiers courts en Markdown pur, éditables directement dans le navigateur.</p>
        </div>
      </div>
    </div>

    <!-- VOLET 1 : LES RÈGLEMENTS GÉNÉRAUX -->
    <div style="margin-bottom: 5rem;">
      <div style="display: flex; align-items: baseline; gap: 1rem; margin-bottom: 1.5rem;">
        <span style="background: rgba(6, 78, 59, 0.1); color: var(--color-primary); font-size: 0.85rem; font-weight: 700; padding: 0.25rem 0.75rem; border-radius: 6px;">Volet 1</span>
        <h2 class="about-block-title" style="margin: 0;">Modifier les règlements internes sans être technicien</h2>
      </div>
      
      <p style="font-size: 1.1rem; line-height: 1.7; color: var(--color-text); margin-bottom: 2rem;">
        Les règlements généraux de COHABITAT.CC sont découpés en articles modulaires dans le répertoire <code>_reglements/</code>. Vous n'avez pas besoin d'installer Git ni de maîtriser le code pour suggérer un amendement.
      </p>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1.5rem; margin-bottom: 2.5rem;">
        <div style="background: #ffffff; border: 1px solid var(--color-border); border-radius: 12px; padding: 1.5rem;">
          <div style="font-size: 1.8rem; margin-bottom: 0.75rem;">1️⃣</div>
          <h3 style="font-size: 1.15rem; color: var(--color-primary); margin-bottom: 0.5rem;">Trouvez l'article à bonifier</h3>
          <p style="font-size: 0.95rem; color: var(--color-muted); line-height: 1.6;">
            Rendez-vous sur la page <a href="/reglements/" style="color: var(--color-accent); font-weight: 600;">Règlements</a> et cliquez sur le bouton <em>« Proposer une modification »</em> au bas de l'article visé.
          </p>
        </div>

        <div style="background: #ffffff; border: 1px solid var(--color-border); border-radius: 12px; padding: 1.5rem;">
          <div style="font-size: 1.8rem; margin-bottom: 0.75rem;">2️⃣</div>
          <h3 style="font-size: 1.15rem; color: var(--color-primary); margin-bottom: 0.5rem;">Éditez dans votre navigateur</h3>
          <p style="font-size: 0.95rem; color: var(--color-muted); line-height: 1.6;">
            Sur GitHub, cliquez sur l'icône de crayon (✏️). Modifiez simplement le texte en français clair sans balises HTML. L'onglet <em>Preview</em> vous montre le résultat immédiat.
          </p>
        </div>

        <div style="background: #ffffff; border: 1px solid var(--color-border); border-radius: 12px; padding: 1.5rem;">
          <div style="font-size: 1.8rem; margin-bottom: 0.75rem;">3️⃣</div>
          <h3 style="font-size: 1.15rem; color: var(--color-primary); margin-bottom: 0.5rem;">Expliquez votre intention</h3>
          <p style="font-size: 0.95rem; color: var(--color-muted); line-height: 1.6;">
            En bas de la page, résumez l'objectif de votre proposition et cliquez sur <strong>« Propose changes »</strong>, puis <strong>« Create Pull Request »</strong>.
          </p>
        </div>

        <div style="background: #ffffff; border: 1px solid var(--color-border); border-radius: 12px; padding: 1.5rem;">
          <div style="font-size: 1.8rem; margin-bottom: 0.75rem;">4️⃣</div>
          <h3 style="font-size: 1.15rem; color: var(--color-primary); margin-bottom: 0.5rem;">Période de relecture (14 j)</h3>
          <p style="font-size: 0.95rem; color: var(--color-muted); line-height: 1.6;">
            Les membres échangent et suggèrent des bonifications. En l'absence d'objections raisonnables, la proposition est adoptée et intégrée au site.
          </p>
        </div>
      </div>

      <div style="background: rgba(6, 78, 59, 0.04); border-left: 4px solid var(--color-primary); padding: 1.25rem 1.5rem; border-radius: 0 12px 12px 0;">
        <h4 style="margin: 0 0 0.5rem; color: var(--color-primary); font-size: 1.05rem;">Qu'est-ce qu'une objection raisonnable au sens sociocratique ?</h4>
        <p style="margin: 0; font-size: 0.95rem; line-height: 1.6; color: var(--color-text);">
          Une objection n'est pas un simple désaccord de goût ou une préférence stylistique. C'est l'exposé d'un <strong>risque concret</strong> que la modification ferait courir aux objectifs de la communauté, à sa santé financière ou à sa conformité légale avec la <em>Loi sur les compagnies</em>. Si une objection est soulevée, le groupe cherche ensemble une formulation alternative qui y répond.
        </p>
      </div>
    </div>

    <!-- VOLET 2 : LES DÉCISIONS DU CONSEIL D'ADMINISTRATION -->
    <div style="margin-bottom: 5rem;">
      <div style="display: flex; align-items: baseline; gap: 1rem; margin-bottom: 1.5rem;">
        <span style="background: rgba(194, 65, 12, 0.1); color: var(--color-accent); font-size: 0.85rem; font-weight: 700; padding: 0.25rem 0.75rem; border-radius: 6px;">Volet 2</span>
        <h2 class="about-block-title" style="margin: 0;">Décisions &amp; Résolutions du Conseil d'administration</h2>
      </div>

      <p style="font-size: 1.1rem; line-height: 1.7; color: var(--color-text); margin-bottom: 1.5rem;">
        En vertu de l'<strong>article 89.1 de la Loi sur les compagnies du Québec (Partie III)</strong>, les administrateurs d'un OBNL peuvent adopter des résolutions écrites par consentement sans avoir à tenir une assemblée formelle en personne :
      </p>

      <blockquote style="margin: 0 0 2rem; padding: 1.25rem 1.5rem; background: #ffffff; border-left: 4px solid var(--color-accent); border-radius: 0 12px 12px 0; font-style: italic; color: var(--color-text); font-size: 1rem; line-height: 1.7;">
        « Une résolution écrite, signée par tous les administrateurs habiles à voter sur cette résolution lors d'une séance du conseil d'administration [...] a la même valeur que si elle avait été adoptée lors d'une telle séance. »
      </blockquote>

      <h3 style="font-size: 1.3rem; color: var(--color-primary); margin-bottom: 1rem;">Le cycle d'une résolution du CA sur GitHub</h3>
      
      <ol style="font-size: 1rem; line-height: 1.8; color: var(--color-text); padding-left: 1.5rem; margin-bottom: 2rem;">
        <li><strong>Dépôt de la proposition :</strong> Un administrateur crée une branche et rédige un fichier Markdown dans <code>ca/resolutions/YYYY-MM-DD-RES-XX.md</code> en s'appuyant sur notre <a href="https://github.com/cohabitat-cc/www.cohabitat.cc/blob/main/ca/resolutions/2026-00-modele-resolution.md" target="_blank" rel="noopener">modèle de résolution</a> (attendus clairs, mandats, montants budgétaires autorisés).</li>
        <li><strong>Ouverture de la Pull Request :</strong> La PR est soumise avec le gabarit dédié <code>resolution_ca.md</code>.</li>
        <li><strong>Délibération asynchrone :</strong> Les administrateurs peuvent poser des questions, exiger des pièces justificatives (devis, analyse juridique) ou proposer des ajustements directement sur les lignes du texte.</li>
        <li><strong>Consentement écrit / Signature électronique :</strong> Chaque administrateur approuve formellement la PR via le bouton <strong>Review changes &gt; Approve</strong> en inscrivant sa mention de consentement légale.</li>
        <li><strong>Adoption &amp; Archivage :</strong> Une fois le consentement unanime obtenu, la PR est fusionnée. Le registre est automatiquement mis à jour et accessible à tous les membres.</li>
      </ol>
    </div>

    <!-- Liens d'action -->
    <div class="bylaws-action-footer">
      <h3>Accéder aux registres et participer</h3>
      <p>Consultez directement les sources Markdown sur GitHub, vérifiez les résolutions passées ou formulez votre première suggestion.</p>
      <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap; margin-top: 1.5rem;">
        <a href="{{ '/reglements/' | relative_url }}" class="action-btn">
          Consulter les règlements
        </a>
        <a href="https://github.com/cohabitat-cc/www.cohabitat.cc/tree/main/ca" target="_blank" rel="noopener" class="btn-secondary" style="padding: 0.85rem 1.8rem; border-radius: 9999px; font-weight: 600; text-decoration: none; display: inline-block;">
          Registre du CA sur GitHub
        </a>
      </div>
    </div>

  </div>
</section>
